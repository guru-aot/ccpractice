from flask import Flask, g, jsonify, request, json, send_file
from flask_restplus import Namespace, Resource, cors
from services.config import app , oidc
from dataaccess.requestsDataAccess import RequestDataAccess
from utils.jsonClassEncoder import JsonClassEncoder
from utils.email import Email
from utils.util import cors_preflight
from datetime import datetime, timedelta
from flask import Blueprint
import os
import glob


REQUESTAPI_BLUEPRINT = Blueprint('REQUESTAPI', __name__, url_prefix='')

API = Namespace('requests', description='requests')

requestDataAccess = RequestDataAccess()
jsonClassEncoder = JsonClassEncoder()
emailservice = Email() 
UploadFolder = os.path.join(app.root_path, 'attachments') 


@API.route('', methods=['GET', 'POST', 'OPTIONS'])
class RequestResource(Resource):
    
    @staticmethod
    @REQUESTAPI_BLUEPRINT.route('/requests/test')
    @oidc.accept_token(True)   
    def get():
        return jsonify("its working!") , 200

    @staticmethod    
    @REQUESTAPI_BLUEPRINT.route('/requests/upload/<requestid>', methods=['GET','POST'])
    @oidc.accept_token(True)
    def file_upload(requestid):  
        fileStorage = request.files['image']
        uploadFolder = UploadFolder + '/' + requestid + '/'
        uploadFolder = uploadFolder.replace('\\','/')
        # uploadFolder = app.config['UPLOAD_FOLDER'] + requestid + '/' 
        if not os.path.isdir(uploadFolder):
            os.mkdir(uploadFolder)
        fileName = fileStorage.filename.split(".")
        fileStorage.save(os.path.join(uploadFolder, fileName[0] + datetime.now().strftime("%m%d%Y%H%M%S") + '.' + fileName[1]))    
        print(' * received form with', request.files['image'])  
        return jsonClassEncoder.encode(True), 200    

    @staticmethod   
    @REQUESTAPI_BLUEPRINT.route('/requests/download/<requestid>')
    @oidc.accept_token(True) 
    def file_download(requestid): 
        folderpath = UploadFolder + '/' + requestid + '/'    
        folderpath = folderpath.replace('\\','/')
        list_of_files = glob.glob(folderpath + '*') # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        latest_file = latest_file.replace("\\", "/")
        # arr = latest_file.split("/")
        # filename = arr[len(arr)-1]
        print(latest_file)  
        try:       
            return send_file(latest_file, as_attachment=False)
        except Exception as e:
            print(e)
            return jsonClassEncoder.encode(False), 500 
    
    @staticmethod   
    @REQUESTAPI_BLUEPRINT.route('/requests/<requestid>', methods=['PUT', 'DELETE'])
    @cors_preflight('GET,POST,OPTIONS,PUT,DELETE') 
    @oidc.accept_token(True) 
    def single_request(requestid):
        response_object = {'status': 'success'}
        if request.method == 'PUT':
            requestjson = request.get_json()
            name = requestjson['name']
            description = requestjson['description']
            status = requestjson['status']
            createdby = requestjson['createdby']   
            updated = requestjson['updated']
            requestaddresult = requestDataAccess.EditRequest(requestid, name, description, status, createdby, updated)
            response_object['message'] = 'Request updated!'
        if request.method == 'DELETE':
            requestaddresult = requestDataAccess.DeleteRequest(requestid)
            response_object['message'] = 'Request removed!'
        if requestaddresult.success == True:
            return jsonClassEncoder.encode(requestaddresult), 200
        else:
            return jsonClassEncoder.encode(requestaddresult), 500

    @staticmethod
    @cors_preflight('GET,POST,OPTIONS')       
    @REQUESTAPI_BLUEPRINT.route('/requests/add', methods=['GET','POST'])    
    @oidc.accept_token(True)  
    def addrequest():
        requestjson = request.get_json()

        name = requestjson['name']
        description = requestjson['description']
        status = requestjson['status']
        createdby = requestjson['createdby']    
        userid = g.oidc_token_info['sub']
        requestaddresult = requestDataAccess.AddRequest(name, description, status, createdby, userid)
        if requestaddresult.success == True:
            emailservice.send('abin.antony@aot-technologies.com','TEST FOI TEST',"REQUEST ADDED")
            return jsonClassEncoder.encode(requestaddresult), 200
        else:
            return jsonClassEncoder.encode(requestaddresult), 500

    @staticmethod    
    @REQUESTAPI_BLUEPRINT.route('/requests/all')
    @cors_preflight('GET,POST,OPTIONS')
    @oidc.accept_token(True)     
    def getallrequests():
        roles = g.oidc_token_info['realm_access']['roles']
        userid = g.oidc_token_info['sub']
        userrole = 'user_role'
        approverrole = 'approver_role'
        if userrole in roles:
            requests = requestDataAccess.GetRequestsByUser(userid)
        elif approverrole in roles:
            requests = requestDataAccess.GetRequestsByRole()
        else:
            requests = requestDataAccess.GetRequests()
        jsondata = json.dumps(requests)
        return jsondata, 200       