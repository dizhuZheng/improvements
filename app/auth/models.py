from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model): 
    __tablename__ = "users" 
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(20), unique=True) 
    email = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)
    roles = db.relationship('Role', back_populates="user")

    def set_password(self, password):  
        self.password_hash = generate_password_hash(password)  

    def validate_password(self, password):  
        return check_password_hash(self.password_hash, password)  
    
    def __repr__(self):
        return self.name
    

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User", back_populates="roles")

    def __repr__(self):
        return self.name
