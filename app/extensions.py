from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from sqlalchemy.orm import DeclarativeBase
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap5
from flask_bcrypt import Bcrypt 
from flask_mail import Mail
from faker import Faker
from flask_ckeditor import CKEditor
from flask_principal import Principal, Permission, RoleNeed

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
migrate = Migrate()
login_manager = LoginManager()
bootstrap = Bootstrap5()
login_manager.session_protection = "strong"
csrf = CSRFProtect()
bcrypt = Bcrypt() 
mail = Mail()
fake = Faker()
ckeditor = CKEditor()
principals = Principal()
admin_permission = Permission(RoleNeed('Admin'))
# poster_permission = Permission(RoleNeed('Editor'))
# default_permission = Permission(RoleNeed('Normal'))
login_manager.login_view = "auth_bp.login"
login_manager.refresh_view = "auth_bp.login"
login_manager.login_message = u'Please log in to access this page.'
login_manager.needs_refresh_message = (
    u"To protect your account, please reauthenticate to access this page."
)
login_manager.needs_refresh_message_category = "info"
