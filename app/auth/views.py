from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose, AdminIndexView
from flask import render_template, redirect, url_for, flash, abort
from flask_login import current_user


class MyView(BaseView):
    @expose('/')
    def index(self):
        return 'Hello World!'
    def is_accessible(self):
        return current_user.is_authenticated


class MyHomeView(AdminIndexView):
    @expose('/home')
    def index(self):
        arg1 = 'Hello'
        return self.render('admin/myhome.html', arg1=arg1)

    
class UserAdmin(ModelView):
    column_list = ('name', 'email', 'roles', 'active')
    column_labels = {'name': 'Username', 'email': 'Email Address', 'roles': 'Role', 'active':'Active'}
    def is_accessible(self):
        return current_user.is_authenticated and current_user.get_id()=='11'
                 
    
class RoleAdmin(ModelView):
    column_list = ('name', 'users')
    def is_accessible(self):
        return current_user.is_authenticated and current_user.get_id()=='11'
                 
