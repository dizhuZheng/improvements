import os 

class Config:
    # SECRET_KEY = os.environ.get("SECRET_KEY")
    # if not SECRET_KEY:
    #   raise ValueError("No SECRET_KEY set for Flask application")
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # DB_SERVER = '192.168.1.56'

    # @property
    # def DATABASE_URI(self):  # Note: all caps
    #     return f"mysql://user@{self.DB_SERVER}/foo"
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join('/Users/dizhu/improvement/app', 'data.db')
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