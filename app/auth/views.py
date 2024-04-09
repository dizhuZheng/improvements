from flask_admin.contrib.sqla import ModelView
from .models import User, Role

class UserAdmin(ModelView):
    column_list = ('name', 'email', 'roles', 'active')
    column_labels = {'name': 'Username', 'email': 'Email Address', 'roles': 'Role', 'active':'Active'}
    

class RoleAdmin(ModelView):
    column_list = ('name')
    column_labels = {'name': 'Role Name'}