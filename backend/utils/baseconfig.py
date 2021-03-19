
import os

from dotenv import find_dotenv, load_dotenv

# this will load all the envars from a .env file located in the project root (api)
load_dotenv(find_dotenv())

class BaseConfig(object):
    """
    Common configuration
    """
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OIDC_ISSUER_URI= os.getenv('OIDC_ISSUER_URI')
    OIDC_OPENID_REALM_CALLBACK = os.getenv('OIDC_OPENID_REALM_CALLBACK')
    BACKEND_SECRET_KEY = os.getenv('BACKEND_SECRET_KEY')
    OIDC_ID_TOKEN_COOKIE_SECURE = os.getenv('OIDC_ID_TOKEN_COOKIE_SECURE')
    OIDC_REQUIRE_VERIFIED_EMAIL = os.getenv('OIDC_REQUIRE_VERIFIED_EMAIL')

class Development(BaseConfig):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = True

class Testing(BaseConfig):
    """
    Testing environment configurations
    """
    DEBUG = False
    TESTING = True    

class Production(BaseConfig):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False


CONFIG = {
    'production': Production,
    'development': Development,
    'testing': Testing,
}