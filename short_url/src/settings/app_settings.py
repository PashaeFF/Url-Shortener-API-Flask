

from msilib.schema import Class
import os

class BaseSettings:

    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DB_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {
        'title':"URL Shortener API",
    }
    SQLALCHEMY_MAX_OVERFLOW = True

app_settings = BaseSettings()