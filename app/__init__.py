import os
from flask import Flask
from .learning_logs import learning_logs_bp
from .auth import auth_bp
from .main import main_bp
from config import config
from .extensions import db
from dotenv import load_dotenv
load_dotenv()

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    db.init_app(app)
    # migrate.init_app(db)
    app.register_blueprint(learning_logs_bp, url_prefix='/learning_logs')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp)
    return app


