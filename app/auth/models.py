from ..extensions import db, bcrypt
from flask_login import UserMixin


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

    def set_password(self, password):  
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')   

    def validate_password(self, password):  
        return bcrypt.check_password_hash(self.password_hash, password)  
    
    def __repr__(self):
        return self.name
    

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    users = db.relationship("User", secondary=user_role_association, back_populates="roles")

    def __repr__(self):
        return self.name
