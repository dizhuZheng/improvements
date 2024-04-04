from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
# from forms import LoginForm
import click
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from app.extensions import db

auth_bp = Blueprint('auth_bp', __name__,template_folder='/templates', static_folder='/static', static_url_path='/assets')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile.html'))

    form = LoginForm()
    if form.validate_on_submit():
        login_user(current_user)
        flash('Logged in successfully.')
        if admin:
            if username == admin.username and admin.validate_password(password):
                login_user(admin, remember)
                flash('Welcome back.', 'info')
                return redirect()
            flash('Invalid username or password.', 'warning')
        else:
            return abort(400)
    return render_template('auth/login.html', form=form)


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return 'it is wrong'
        return redirect(url_for('index'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("login"))
    return render_template("sign_up.html")


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))


@auth_bp.cli.command()
@click.option('--username', prompt=True, help='The username used to login.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='The password used to login.')
def admin(username, password):
    """Create user."""
    db.create_all()

    user = User.query.first()
    if user is not None:
        click.echo('Updating user...')
        user.username = username
        user.set_password(password)  # 设置密码
    else:
        click.echo('Creating user...')
        user = User(username=username, name='Admin')
        user.set_password(password)  # 设置密码
        db.session.add(user)

    db.session.commit()  # 提交数据库会话
    click.echo('Done.')