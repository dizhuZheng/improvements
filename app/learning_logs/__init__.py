from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

learning_logs_bp = Blueprint('learning_logs_bp', __name__, template_folder='/templates', static_folder='/static', static_url_path='/assets')

@learning_logs_bp.route('/')
def index():
  return "this is an learning log blueprint hahaha"