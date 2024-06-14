import os 
from dotenv import load_dotenv
load_dotenv()
from datetime import timedelta 

class Config:
    FLASK_ADMIN_SWATCH = 'journal'
    SECRET_KEY = os.environ.get("SECRET_KEY")
    if not SECRET_KEY:
      raise ValueError("No SECRET_KEY set for Flask application")
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') 
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') 
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_SERVER = 'smtp.gmail.com'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SESSION_COOKIE_SAMESITE = "strict"
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=20)
    REMEMBER_COOKIE_SAMESITE = "strict"
    CKEDITOR_PKG_TYPE = 'basic'
    REMEMBER_COOKIE_SECURE = True
    ADMIN_USERS = ["admin"]
    

    @property
    def DATABASE_URI(self):  # Note: all caps
        return f"mysql://user@{self.DB_SERVER}/foo"

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    # set optional bootswatch theme
    FLASK_ADMIN_SWATCH = 'journal'
    # prefix + os.path.join(basedir, 'data-dev.db')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
    PRODUCTION = True
    # WTF_CSRF_ENABLED = False
  # SQLALCHEMY_DATABASE_URI = xxx

config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}