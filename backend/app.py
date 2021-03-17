
import uuid
from flask import Flask, g, jsonify, request, json
from flask_oidc import OpenIDConnect
from flask_cors import CORS, cross_origin
from entities.request import Request
from dataaccess.requestsDataAccess import RequestDataAccess
from utils.jsonClassEncoder import JsonClassEncoder
from config import init_app
from utils.util import cors_preflight , reviewer, approver , hasrole

# configuration
DEBUG = True

app = init_app()

requestDataAccess = RequestDataAccess()
jsonClassEncoder = JsonClassEncoder()

oidc = OpenIDConnect(app)

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]


@app.route('/')
def home():
    if oidc.user_loggedin:
        return("Hello,%s"%oidc.user_getfield('email'))
    else:
        return 'Welcome, please <a href="/dashboard">Login</a>'

@app.route('/dashboard')
@oidc.require_login
@cross_origin()
def dashboard():
    userinfo = oidc.user_getinfo(['email','preferred_username','sub'])

    username = userinfo.get('preferred_username')
    email  = userinfo.get('email')
    userid = userinfo.get('sub')

    return("This is your dashboard, %s and your email is %s! and UserId is %s"%(username,email,userid))

@app.route('/user')
@oidc.accept_token(True)
def user():
    email = g.oidc_id_token['email']
    userid = g.oidc_id_token['sub']
    username = g.oidc_id_token['preferred_username']
    userobject = {'Name':username,'Email':email,'ID':userid}
    response = jsonify(userobject)
    return response

# sanity check route
@app.route('/ping', methods=['GET'])
@oidc.accept_token(True)
@hasrole('approver_role')
def ping_pong():
    return jsonify('pong!')

def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


@app.route('/books')
@cors_preflight('GET,POST,OPTIONS')
@oidc.accept_token(True)
@hasrole('reviewer_role')
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)



@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)

@app.route('/requests/add', methods=['POST', 'GET'])
def addrequest():
    requestjson = request.get_json()

    name = requestjson['name']
    description = requestjson['description']
    status = requestjson['status']

    requestaddresult = requestDataAccess.AddRequest(name, description, status)
    if requestaddresult.success == True:
        return jsonClassEncoder.encode(requestaddresult), 200
    else:
        return jsonClassEncoder.encode(requestaddresult), 500

@app.route('/requests/all', methods=['GET'])
def getallrequests():
    requests = requestDataAccess.GetRequests()
    jsondata = json.dumps(requests)
    return jsondata, 200


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")