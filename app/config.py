from datetime import timedelta
from dotenv import load_dotenv
import os

class ConfigBase:
    SQLALCHEMY_DATABASE_URI = None

    SECURITY_PASSWORD_HASH = None
    SECURITY_PASSWORD_SALT = None
    SECRET_KEY = None

    JWT_SECRET_KEY = None
    JWT_ACCESS_TOKEN_EXPIRES = None

    SECURITY_REGISTERABLE = False
    SECURITY_SEND_REGISTER_EMAIL = False

    WTF_CSRF_ENABLED = False

    DEBUG = False


class DevelopmentConfig(ConfigBase):
    SQLITE_DB_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../db_directory')

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(SQLITE_DB_DIR, 'assignment.sqlite3')

    SECURITY_PASSWORD_HASH = 'bcrypt'

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)

    SECURITY_REGISTERABLE = True

    DEBUG = True

    def __init__(self):
        load_dotenv()
        self.SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT')
        self.SECRET_KEY = os.getenv('SECRET_KEY')
        self.JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')