from flask import Blueprint, render_template, redirect, url_for, flash, request, Response
from .forms import LoginForm, RegisterForm, SettingForm
from app.auth.models import User, Role
from flask_login import login_user, logout_user, login_required, current_user, fresh_login_required
from ..extensions import login_manager, db, bcrypt, mail
from flask_mail import Message
from flask_principal import identity_changed, Identity, current_app
from .permission import admin_authority


auth_bp = Blueprint('auth_bp', __name__,template_folder='./templates', static_folder='./static', static_url_path='./assets')


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    users = db.session.query(User).all()
    if email not in users:
        return
    
@auth_bp.route('/admin')
@admin_authority.require()
def do_admin_index():
    return Response('Only if you are an admin')


@auth_bp.route('/test', methods=['GET', 'POST'])
def index():
    with admin_authority.require():
        return Response('Only if you are admin')
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
                login_user(user, remember=True)
                identity_changed.send(current_app._get_current_object(), identity=Identity(user.id))
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
    if form.validate_on_submit():
        name = form.name.data
        user = User.query.filter_by(name=name).first()
        email = form.email.data
        info = User.query.filter_by(email=email).first()
        if user or info :
            error = "sorry, user existed already."
        else:
            password = form.password.data
            # msg = Message("Hello",
            #     sender="dizhu210@gmail.com",
            #     recipients=[email])
            # mail.send(msg)
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8') 
            new_user = User(email=email, name=name, password_hash=hashed_password)
            db.session.add(new_user)
            db.session.flush()
            role = Role.query.filter_by(name='Normal').first()
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


# @route('/admin/dashboard')    # @route() must always be the outer-most decorator
# @roles_required('Admin')
# def admin_dashboard():
    # render the admin dashboard
@auth_bp.route('/error')
def errors():
    pass


@auth_bp.route("/settings", methods=['GET', 'POST'])
@fresh_login_required
def settings():
    form = SettingForm(request.form, obj=current_user)
    error = ""
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.email = form.email.data
        current_user.password = form.password.data
        current_user.verified = True
        db.session.commit()
        db.session.commit()
        flash('All your info has been updated !')
        return redirect(url_for('auth_bp.login'))
    return render_template('settings.html', form=form, error=error, current_user=current_user)

        
@auth_bp.route("/lost_and_find")
@fresh_login_required
def account_recovery():
    pass