from flask import current_app, Blueprint, render_template, abort
from jinja2 import TemplateNotFound

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

@auth_bp.route('/')
def index():
  # return render_template(current_app.config['INDEX_TEMPLATE'])
  return'hello dizhu'