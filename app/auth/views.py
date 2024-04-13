from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class UserAdmin(ModelView):
    column_list = ('name', 'email', 'roles', 'active')
    column_labels = {'name': 'Username', 'email': 'Email Address', 'roles': 'Role'}
    

class RoleAdmin(ModelView):
    column_list = ('name', 'user')
    column_labels = {'name': 'Role Name'}
    # column_searchable_list = ['name']

