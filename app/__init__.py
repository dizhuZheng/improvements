from flask import Flask
from .learning_logs import learning_logs_bp
from .auth import auth_bp
from .main import main_bp
from config import config 

# 然后根据自己的需要来create_app('development')之类的得到app，这样的一个app是自带了一整套运行用的插件以及合适的配置的，就可以方便地让app.run了。
def create_app(config_mode):
    app = Flask(__name__)
    app.config.from_object(config[config_mode])

    # from yourapplication.model import db
    
    # db.init_app(app)

    # from yourapplication.views.admin import admin
    # from yourapplication.views.frontend import frontend
    # app.register_blueprint(admin)
    # app.register_blueprint(frontend)
    app.register_blueprint(learning_logs_bp, url_prefix='/learning_logs')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp)
    # app.register_blueprint(main_bp, url_prefix='/home')
    return app


# from flask import Flask,render_template
# from flask.ext.bootstrap import Bootstrap
# from flask.exit.moment import Moment
# from flask.ext.sqlalchemy import SQLAlchemy
# from config import config    #config就默认是上面写过的那个config啦

# bootstrap = Bootstrap()
# moment = Moment()
# db = SQLAlchemy()    #这里创建的三个扩展组件的对象都还是空对象，没有约束具体的app对象

# def create_app(config_mode):
#     app = Flask(__name__)
#     app.config.from_object(config[config_mode])
#     config[config_mode].init_app(app)

#     bootstrap.init_app(app)
#     moment.init_app(app)
#     db.init_app(app)
#     #现在三个插件约束了app

#     '''要在这里添加一些路由和自定义错误处理的信息，按照下文的说明，可以注册一个蓝本对象'''    from .main import main as main_blueprint    app.register_blueprint(main_blueprint)

#     return app
# 这个方法的缺点是在导入时无法在蓝图中使用应用对象。但是你可以在一个请求 中使用它。如何通过配置来访问应用？使用 current_app:
# from flask import current_app, Blueprint, render_template
# admin = Blueprint('admin', __name__, url_prefix='/admin')

# @admin.route('/')
# def index():
#     return render_template(current_app.config['INDEX_TEMPLATE'])


# 最好分别创建扩展和应用工厂，这样扩展对象就不会过早绑定到应用。



# from flask import Flask
# from personalBlog.settings import config

# def create_app(config_name=None):
#     if config_name is None:
#         config_name = os.getenv('FLASK_CONFIG', 'development')
        
#     app = Flask('personalBlog')
#     app.config.from_object(config[config_name])

#     register_logging(app)  # 注册日志处理器
#     register_extensions(app)  # 注册扩展（扩展初始化）
#     register_blueprints(app)  # 注册蓝本
#     register_commands(app)  # 注册自定义shell命令
#     register_errors(app)  # 注册错误处理函数
#     register_shell_context(app)  # 注册错误处理函数
#     register_template_context(app)  # 注册模板上下文处理函数
    
#     return app
# def register_logging(app):
#     pass  #后续介绍日志

# def register_extensions(app):
#     bootstrap.init_app(app)
#     db.init_app(app)
#     ckeditor.init_app(app)
#     mail.init_app(app)
#     moment.init_app(app)

# def register_blueprints(app):
#     app.register_blueprint(auth, url_prefix = '/auth')

# def register_shell_context(app):
#     @app.shell_context_processor
#     def make_shell_context():
#         return dict(db = db)

# def register_template_context(app):
#     pass

# def register_errors(app):
#     @app.errorhandler(400)
#     def bad_request(e):
#         return render_template('errors/400.html'), 400

# def register_commands(app):
#     pass
