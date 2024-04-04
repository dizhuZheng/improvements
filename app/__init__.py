import os
from flask import Flask, render_template
from .learning_logs import learning_logs_bp
from .auth import auth_bp
from config import config
from .extensions import db, migrate, login_manager
from .auth.models import User
from dotenv import load_dotenv
load_dotenv()

def page_not_found(e):
  return render_template('404.html'), 404

def internal_server_error(e):
  return render_template('500.html'), 500

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    migrate.init_app(app, db)
    # login_manager.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(learning_logs_bp, url_prefix='/learning_logs')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)
    return app
