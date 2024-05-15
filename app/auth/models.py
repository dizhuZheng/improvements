from ..extensions import db, bcrypt, login_manager
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
    about = db.Column(db.Text(), nullable=True)

    # @property
    # def email(self):
    #     return self.email   

    # @email.setter
    # def email(self, value):
    #     self.email = value  # on user.email='xyz': set user.email_address='xyz'

    # @property
    # def password(self):
    #     return self.password_hash
    
    # @password.setter
    # def password(self, password):  
    #     self.password_hash = password

    # @property
    # def name(self):  
    #     return self.name
     
    # @name.setter
    # def name(self, name):  
    #     self.name = name
      
    def validate_password(self, password):  
        return bcrypt.check_password_hash(self.password_hash, password)  
    
    def __repr__(self):
        return self.name

@login_manager.user_loader
def load_user(id):
    user = User.query.get(int(id))
    return user

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized', 401


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    users = db.relationship("User", secondary=user_role_association, back_populates="roles")

    def __repr__(self):
        return self.name
