
# entities\request.py
from flask_sqlalchemy import SQLAlchemy
import flask_login
import json

db = SQLAlchemy()
class Request(db.Model):
    __tablename__ = 'Requests' # Name of the table in our database
    # Defining the columns
    requestid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    status = db.Column(db.String(25), unique=False, nullable=True)
    def get_id(self):
        return text_type(self.requestid)

