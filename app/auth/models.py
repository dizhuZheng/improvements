from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model): 
    __tablename__ = "users" 
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(20), unique=True) 
    email = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary='user_roles')
    user_emails = db.relationship('UserEmail')
    
    def set_password(self, password):  
        self.password_hash = generate_password_hash(password)  

    def validate_password(self, password):  
        return check_password_hash(self.password_hash, password) 
    
    def __repr__(self):
        return '<User %r>' % self.username


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)


class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))


class UserEmail(db.Model):
    __tablename__ = 'user_emails'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', uselist=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.DateTime())
    is_primary = db.Column(db.Boolean(), nullable=False, server_default='0')

