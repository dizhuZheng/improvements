import os 
from dotenv import load_dotenv
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    if not SECRET_KEY:
      raise ValueError("No SECRET_KEY set for Flask application")
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    
    @property
    def DATABASE_URI(self):  # Note: all caps
        return f"mysql://user@{self.DB_SERVER}/foo"

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    # prefix + os.path.join(basedir, 'data-dev.db')

class TestingConfig(Config):
    TESTING = True
  # SQLALCHEMY_DATABASE_URI = xxxx

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