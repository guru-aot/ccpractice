
# entities\databaseSessionManager.py
import json
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_CONNECTION = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_CONNECTION, echo=True)

# create a Session
Session = sessionmaker(bind=engine)

class SessionManager(object):
    def __init__(self):
        self.session = Session()