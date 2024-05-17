from flask import Blueprint, render_template, redirect, url_for, flash, abort
from flask_login import login_user, logout_user, login_required, current_user
from ..extensions import login_manager, db, bcrypt

main_bp = Blueprint('main_bp', __name__,template_folder='./templates', static_folder='./static', static_url_path='./assets')

@main_bp.route('/', methods=['GET'])
def main():
  return render_template('index.html')

