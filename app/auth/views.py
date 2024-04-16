from flask_admin.contrib.sqla import ModelView

class UserAdmin(ModelView):
    column_list = ('name', 'email', 'roles', 'active')
    column_labels = {'name': 'Username', 'email': 'Email Address', 'roles': 'Role', 'active':'Active'}

    
class RoleAdmin(ModelView):
    column_list = ('name', 'user')
    column_labels = {'name': 'Role Name'}
    # column_searchable_list = ['name']
