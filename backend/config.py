import os
from flask import Flask
from flask_cors import CORS, cross_origin
from flask_oidc import OpenIDConnect
from utils.db import db
from utils.exception_handler import ExceptionHandler
from utils.logger import setup_logging
from utils.baseconfig import CONFIG, BaseConfig

from dotenv import find_dotenv, load_dotenv

setup_logging(os.path.join(BaseConfig.PROJECT_ROOT, 'logging.conf'))  # important to do this first

def init_app(run_mode=os.getenv('FLASK_ENV', 'development')):
    app = Flask(__name__)
    app.config.from_object(CONFIG[run_mode])
    CORS(app) 

# def init_app():
#     app = Flask(__name__)
#     # app.config.from_object(CONFIG[run_mode])
#     CORS(app) 

    app.config.update({
        'SECRET_KEY': 'FOICLIENTAPP',          
        'OIDC_CLIENT_SECRETS': 'client_secrets.json',
        'OIDC_ID_TOKEN_COOKIE_SECURE': BaseConfig.OIDC_ID_TOKEN_COOKIE_SECURE,
        'OIDC_REQUIRE_VERIFIED_EMAIL': BaseConfig.OIDC_REQUIRE_VERIFIED_EMAIL,
        'OIDC_VALID_ISSUERS': [BaseConfig.OIDC_ISSUER_URI],
        'OIDC_OPENID_REALM': BaseConfig.OIDC_OPENID_REALM_CALLBACK,
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'SQLALCHEMY_DATABASE_URI':BaseConfig.SQLALCHEMY_DATABASE_URI,
      
    })
    ExceptionHandler(app)
    db.init_app(app)    
    return app

