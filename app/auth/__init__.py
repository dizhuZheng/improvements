from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from .forms import LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from app.auth.models import User
from flask_login import login_user, logout_user, login_required, current_user
from ..extensions import login_manager

auth_bp = Blueprint('auth_bp', __name__,template_folder='./templates', static_folder='./static', static_url_path='./assets')


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized', 401


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized', 401


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    message = ""
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        user = User.query.filter_by(name=name).first()
        if user:
          if user.password_hash == password:
              login_user(user)
              message = "haha"
              return redirect(url_for("auth_bp.protected"))
          else:
              message = "Ah-oh, your password is wrong."
        else:
            message = 'No exsting user.'
    return render_template("login.html", form=form, message=message)


@auth_bp.route('/protected')
@login_required
def protected():
    message = "success!"
    return render_template('profile.html', current_user=current_user, message=message)
# @auth_bp.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         name = request.form.get('name')
#         password = request.form.get('password')

#     if user: # if a user is found, we want to redirect back to signup page so user can try again
#         return 'it is wrong'
#         return redirect(url_for('index'))

#     # create a new user with the form data. Hash the password so the plaintext version isn't saved.
#     new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

#     # add the new user to the database
#     db.session.add(new_user)
#     db.session.commit()
#     return redirect(url_for("login"))
#     return render_template("sign_up.html")


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out'


@auth_bp.route("/settings")
@login_required
def settings():
    pass
