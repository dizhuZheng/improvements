from ..extensions import db, bcrypt, login_manager
from flask_login import UserMixin, AnonymousUserMixin
from itsdangerous import URLSafeTimedSerializer
import os


user_role_association = db.Table(
    'user_role',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))
)


class User(UserMixin, db.Model): 
    __tablename__ = "users" 
    id = db.Column(db.Integer, primary_key=True)  
    name = db.Column(db.String(20), unique=True) 
    email = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)
    roles = db.relationship('Role', secondary=user_role_association, back_populates="users")
    about = db.Column(db.Text(), nullable=True)
    
    def __init__(self, name, email, password_hash, about):
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.about = about
    
    def generate_confirmation_token(self):
        serializer = URLSafeTimedSerializer(os.getenv('SECRET_KEY'))
        return serializer.dumps(self.email, salt=os.getenv('SECURITY_PASSWORD_SALT'))

    def confirm_token(token, expiration=3600):
        serializer = URLSafeTimedSerializer(os.getenv('SECRET_KEY'))
        try:
            email = serializer.loads(
                token,
                salt=os.getenv('SECURITY_PASSWORD_SALT'),
                max_age=expiration
            )
        except:
            return False
        return email

    def validate_password(self, password):  
        return bcrypt.check_password_hash(self.password_hash, password) 
    
    def __str__(self):
        return f'{self.name} and the roles are {self.roles}'
    
    def __repr__(self): 
        return f'Role(\'{self.name}\', {self.roles})'
    
       
@login_manager.user_loader
def load_user(id):
    user = User.query.get(int(id))
    return user


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized', 401


class AnonymousUser(AnonymousUserMixin):

    def can(self, permissions):
        return False

    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    users = db.relationship("User", secondary=user_role_association, back_populates="roles")

    def __init__(self, name): 
        self.name = name 

    def __str__(self):
        return f'{self.name}'
    
    def __repr__(self): 
        return f'Role(\'{self.name}\')'
