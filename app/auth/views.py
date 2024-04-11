from flask_admin.contrib.sqla import ModelView
from .models import User, Role
from flask_login import current_user


class UserAdmin(ModelView):
    column_list = ('name', 'email', 'roles', 'active')
    column_labels = {'name': 'Username', 'email': 'Email Address', 'roles': 'Role', 'active':'Active'}
    # column_searchable_list = ['name', 'email']


class RoleAdmin(ModelView):
    column_list = ('name')
    column_labels = {'name': 'Role Name'}
    # column_searchable_list = ['name']


# class ManagerView(ModelView):
#     def is_accessible(self):
#         return current_user.is_authenticated and current_user.role.name == 'Admin'
#     can_create = False
#     column_labels = {
#         'id':u'序号',
#         'title' : u'新闻标题',
#         'timestamp':u'发布时间',
#         'count':u'浏览次数',
#         'content':u'新闻内容'
#     }
#     column_list = ('id', 'title','timestamp','count','content')
