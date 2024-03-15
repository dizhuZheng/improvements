import os 

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI')
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