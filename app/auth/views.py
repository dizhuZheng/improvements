from flask_admin.contrib.sqla import ModelView
from flask_admin import expose, AdminIndexView, BaseView
from flask import redirect, url_for, request, flash
from flask_login import current_user
from . import admin

class MyView(AdminIndexView):
    @expose('/')
    @admin.require(http_exception=403)
    def index(self):
        arg1 = 'Hello'
        return self.render('admin/myhome.html', arg1=arg1)
    @expose('/test/')
    def test(self):
        return self.render('admin/test.html')
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("main.index"))


        
    