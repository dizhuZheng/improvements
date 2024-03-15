from flask import current_app, Blueprint, render_template, abort
from jinja2 import TemplateNotFound

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():
  # return render_template(current_app.config['INDEX_TEMPLATE'])
  return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

