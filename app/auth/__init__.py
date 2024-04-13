from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from .forms import LoginForm
import click
from ..extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user, UserMixin
from app.extensions import login_manager

auth_bp = Blueprint('auth_bp', __name__,template_folder='./templates', static_folder='./static', static_url_path='./assets')

# @login_manager.request_loader
# def request_loader(request):
#     email = request.form.get('email')
#     if email not in users:
#         return

#     user = User()
#     user.id = email
#     return user

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile.html'))
    form = LoginForm()
    return render_template('login.html', form=form)
    if form.validate_on_submit():
        login_user(current_user)
        flash('Logged in successfully.')
        # if admin:
        #     if username == admin.username and admin.validate_password(password):
        #         login_user(admin, remember)
        #         flash('Welcome back.', 'info')
        #         return redirect()
        #     flash('Invalid username or password.', 'warning')  
        return abort(400)
    return render_template('profile.html', form=form)



# # @auth_bp.route('/login', methods=['GET', 'POST'])
# # def login():
# #     if request.method == 'GET':
# #         return '''
# #                <form action='login' method='POST'>
# #                 <input type='text' name='email' id='email' placeholder='email'/>
# #                 <input type='password' name='password' id='password' placeholder='password'/>
# #                 <input type='submit' name='submit'/>
# #                </form>
# #                '''

# #     email = request.form['email']
# #     if email in users and flask.request.form['password'] == users[email]['password']:
# #         user = User()
# #         user.id = email
# #         flask_login.login_user(user)
# #         return flask.redirect(flask.url_for('protected'))

# #     return 'Bad login'


# @app.route('/protected')
# @flask_login.login_required
# def protected():
#     return 'Logged in as: ' + flask_login.current_user.id

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


# @login_manager.unauthorized_handler
# def unauthorized_handler():
#     return 'Unauthorized', 401