from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from sqlalchemy.orm import DeclarativeBase
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap5

class Base(DeclarativeBase):
  pass


db = SQLAlchemy(model_class=Base)
migrate = Migrate()
login_manager = LoginManager()
bootstrap = Bootstrap5()
login_manager.session_protection = "strong"
csrf = CSRFProtect()
login_manager.login_view = "login"
# login_manager.login_message_category = "info"
