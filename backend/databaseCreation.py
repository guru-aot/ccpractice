# databaseCreation.py
# Author : Andre Baldo (http://github.com/andrebaldo/)
# Make sure that you have a SQL Server runing in your local host, check also the instance
# name, in some instalations the server path will be 'localhost/SQLEXPRESS' in this case, 
# update the SERVER variable below accordingly
# This script creates the tables User and UserSession, just execute:$python databaseCreation.py
# from your command pront, tested just on Windows.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import json
import os
import datetime

app = Flask(__name__)

workingDirectory = os.getcwd()
configFile = os.path.join(workingDirectory, 'config.json')

with open(configFile, 'r') as jsonConfig:
    config = json.load(jsonConfig)

DATABASE_CONNECTION = config['database_connection_string']
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION

db = SQLAlchemy(app)


import flask_login


class Request(db.Model):
    # Name of the table in our database
    __tablename__ = 'Requests' 
    # Defining the columns
    requestid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    status = db.Column(db.String(25), unique=False, nullable=True)  
    createdby = db.Column(db.String(25), unique=False, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now().isoformat())
    updated_at = db.Column(db.TIMESTAMP, default=datetime.datetime.now().isoformat())
    updated = db.Column(db.Boolean, default=False)
    userid = db.Column(UUID(as_uuid=True), unique=False, nullable=False)
    def get_id(self):
        return text_type(self.requestid)

db.create_all()
db.session.commit()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")