from flask import Blueprint, render_template, redirect, url_for, flash, request
from .forms import LoginForm, RegisterForm, DemoForm
from app.auth.models import User, Role
from flask_login import login_user, logout_user, login_required, current_user
from ..extensions import login_manager, db, bcrypt, csrf

auth_bp = Blueprint('auth_bp', __name__,template_folder='./templates', static_folder='./static', static_url_path='./assets')

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized', 401


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth_bp.route('/test', methods=['GET', 'POST'])
@csrf.exempt
def index():
    if request.method == 'POST':  
            name = request.form.get('name')  
            occupation = request.form.get('occupation')
            flash('Item created.')  
            return redirect(url_for('main_bp.main'))  
    return render_template("test.html")


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = ""
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        user = User.query.filter_by(name=name).first()
        if user:
            if bcrypt.check_password_hash(user.password_hash, password):
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect(url_for("auth_bp.protected"))
            else:
              error = "Ah-oh, your password is wrong."
        else:
            error = 'No exsting user.'
    return render_template("login.html", form=form, error=error)


@auth_bp.route('/protected')
@login_required
def protected():
    message = "success!"
    return render_template('profile.html', current_user=current_user, message=message)


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    error = ""
    if request.method == 'POST':
        if form.validate_on_submit():
            name = form.name.data
            user = User.query.filter_by(name=name).first()
            email = form.email.data
            info = User.query.filter_by(email=email).first()
            if user or info:
                error = 'user already exsited.'
            else:
                password = form.password.data
                email = form.email.data
                hashed_password = bcrypt.generate_password_hash(password).decode('utf-8') 
                new_user = User(email=email, name=name, password_hash=hashed_password)
                db.session.add(new_user)
                db.session.flush()
                role = db.session.query(Role)[1]
                new_user.roles.append(role)
                role.users.append(new_user)
                db.session.commit()
                flash('You were successfully registered')
                return redirect(url_for('auth_bp.login'))
    return render_template("signup.html", form=form, error=error)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out'



@auth_bp.route('/error')
def errors():
    pass


@auth_bp.route("/settings")
@login_required
def settings():
    pass


@auth_bp.route("/lost_and_find")
def account_recovery():
    pass