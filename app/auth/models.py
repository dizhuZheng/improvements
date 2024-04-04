from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):  
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(20)) 
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100))
    des = db.Column(db.String, nullable=True)

