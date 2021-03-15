from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


# by convention in the Flask community these are lower case,
# whereas pylint wants them upper case
ma = Marshmallow()  # pylint: disable=invalid-name
db = SQLAlchemy()  # pylint: disable=invalid-name