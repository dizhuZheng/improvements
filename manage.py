from app import create_app
import os
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

if __name__ == '__main__':
    app = create_app()
    # migrate = Migrate()
    app.run()