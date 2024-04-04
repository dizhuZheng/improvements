from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass


db = SQLAlchemy(model_class=Base)
migrate = Migrate()
login_manager = LoginManager()
