import os
from flask import Flask, render_template, jsonify, request
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
import logging
import signal
from .background_thread import BackgroundThreadFactory, TASKS_QUEUE
from flask_cors import CORS


logging.basicConfig(level=logging.INFO, force=True)

load_dotenv()

def page_not_found(e):
  return render_template('404.html'), 404


def internal_server_error(e):
  return render_template('500.html'), 500


def unauthorized(e):
    return render_template('401.html'), 401

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    app = Flask(__name__, static_folder="dist/static", template_folder="dist", static_url_path="/static")
    app.config.from_object(config[config_name])
    CORS(app, resources={r'/*': {'origins': '*'}})
    register_extensions(app)
    with app.app_context():
        db.create_all()
    # sanity check route
    @app.route('/ping', methods=['GET'])
    def ping_pong():
        return jsonify('pong!')
    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def index(path):
        return render_template("base.html")

    # @app.route('/task', methods=['POST'])
    # def submit_task():
    #     task = request.json
    #     logging.info(f'Received task: {task}')

    #     TASKS_QUEUE.put(task)
    #     return jsonify({'success': 'OK'})

    # notification_thread = BackgroundThreadFactory.create('notification')

    # this condition is needed to prevent creating duplicated thread in Flask debug mode
    # if not (app.debug or os.environ.get('FLASK_ENV') == 'development') or os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
    #     notification_thread.start()

    #     original_handler = signal.getsignal(signal.SIGINT)

    #     def sigint_handler(signum, frame):
    #         notification_thread.stop()

            # wait until thread is finished
            # if notification_thread.is_alive():
            #     notification_thread.join()

            # original_handler(signum, frame)

        # try:
        #     signal.signal(signal.SIGINT, sigint_handler)
        # except ValueError as e:
        #     logging.error(f'{e}. Continuing execution...')
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
    

