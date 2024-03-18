from flask import current_app, Blueprint, render_template, abort
from jinja2 import TemplateNotFound

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

@auth_bp.route('/login')
def login():
  # return render_template(current_app.config['INDEX_TEMPLATE'])
  return render_template('login.html')


@auth_bp.route('/signup')
def signup():
    return render_template('signup.html')


@auth_bp.route('/logout')
def logout():
    return 'log out'