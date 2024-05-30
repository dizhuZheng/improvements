import os
from flask import Flask, render_template, g, session
from .learning_logs.views import learning_logs_bp
from .auth import auth_bp
from .auth.models import User, Role
from .main import main_bp
from config import config
from flask_admin import Admin
from .extensions import db, migrate, login_manager, csrf, ckeditor
from dotenv import load_dotenv
from .auth.views import MyView
from flask import render_template
from app.extensions import login_manager, db, bootstrap, bcrypt, mail, principals
from flask_admin.contrib.sqla import ModelView

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
    register_extensions(app)
    with app.app_context():
        db.create_all()
    return app


def register_extensions(app):
    db.init_app(app)
    bootstrap.init_app(app)
    csrf.init_app(app)
    mail.init_app(app)
    bcrypt.init_app
    principals.init_app(app)
    ckeditor.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    app.register_blueprint(main_bp, url_prefix='/')
    app.register_blueprint(learning_logs_bp, url_prefix='/learning_logs')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)
    admin = Admin(app, name='Daily Improvement', template_mode='bootstrap3', index_view = MyView())
    admin.add_view(ModelView(Role, db.session, category="Manage"))
    admin.add_view(ModelView(User, db.session, category="Manage"))
    