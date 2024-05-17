from flask import Blueprint, render_template, redirect, url_for, flash, \
request, Response, session, current_app, abort, g
from .forms import LoginForm, RegisterForm, SettingForm
from app.auth.models import User, Role
from flask_login import login_user, logout_user, login_required, current_user, \
    fresh_login_required
from ..extensions import login_manager, db, bcrypt, mail
from flask_mail import Message
from flask_principal import Permission, Identity, AnonymousIdentity, \
     identity_changed, identity_loaded, UserNeed, RoleNeed, ActionNeed
from urllib.parse import urlparse, urljoin


auth_bp = Blueprint('auth_bp', __name__,template_folder='./templates', static_folder='./static', static_url_path='./assets')


# Needs
be_admin = RoleNeed('Admin')
to_sign_in = ActionNeed('Log In')
# Permissions
user = Permission(to_sign_in)
user.description = "User's permissions"
admin = Permission(be_admin)
admin.description = "Admin's permissions"
apps_needs = [be_admin, to_sign_in]
apps_permissions = [admin, user]

# @login_manager.request_loader
# def request_loader(request):
#     email = request.form.get('email')
#     users = db.session.query(User).all()
#     if email not in users:
#         return

@identity_loaded.connect
def on_identity_loaded(sender, identity):
    identity.user = current_user
    # Add the UserNeed to the identity
    if hasattr(current_user, 'id'):
        identity.provides.add(UserNeed(current_user.id))
    if hasattr(current_user, 'roles'): 
        for role in current_user.roles: 
            identity.provides.add(RoleNeed(role.name)) 


def redirect_url(default='main_bp.main'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("You've already logged in ! " + current_user.name)
        return redirect(redirect_url())
    form = LoginForm()
    error = ""
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        user = User.query.filter_by(name=name).first() or User.query.filter_by(email=name).first()
        if user:
            if bcrypt.check_password_hash(user.password_hash, password):
                if form.remember.data == True:
                    login_user(user, remember=True)
                else:
                    login_user(user)
                session['logged_in']=True
                session["name"] = request.form.get("name")
                identity_changed.send(current_app._get_current_object(),
                                  identity=Identity(user.id))
                return redirect(url_for("auth_bp.protected"))
            else:
              error = "Ah-oh, your password is wrong."
        else:
            error = 'No exsting user.'
    return render_template("login.html", form=form, error=error)


@auth_bp.route('/admin')
@admin.require(http_exception=403)
def admin():
    return render_template('test.html')


@auth_bp.route('/protected')
@login_required
def protected():
    if not session.get("name"):
        flash ("Your session has expired!")
        return redirect(url_for('auth_bp.login'))
    message = "success!"
    return render_template('profile.html', current_user=current_user, message=message)


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        flash("You've already logged in ! " + current_user.name)
        return redirect(redirect_url())
    form = RegisterForm()
    error = ""
    if form.validate_on_submit():
        name = form.name.data
        user = User.query.filter_by(name=name).first()
        email = form.email.data
        info = User.query.filter_by(email=email).first()
        if user or info :
            error = "sorry, user existed already. Want to log in instead ?"
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
    flash("You've logged out !")
    for key in ('identity.name', 'identity.auth_type'):
        session.pop(key, None)
    # Tell Flask-Principal the user is anonymous
    identity_changed.send(current_app._get_current_object(),
                          identity=AnonymousIdentity())
    session.pop('name')
    next = request.args.get('next')
    # if not is_safe_url(next):
    #     return abort(400)
    return redirect(next or '/')


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
        flash('All your info has been updated ! You have to log in again')
        return redirect(url_for('auth_bp.login'))
    return render_template('settings.html', form=form, error=error, current_user=current_user)

        
@auth_bp.route("/lost_and_find")
@fresh_login_required
def account_recovery():
    pass

