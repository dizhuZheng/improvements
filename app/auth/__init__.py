from flask import Blueprint, render_template, redirect, url_for, flash, \
request, session, current_app, abort
from .forms import LoginForm, RegisterForm, FormResetPasswordMail
from app.auth.models import User, Role
from flask_login import login_user, logout_user, login_required, current_user, \
    fresh_login_required
from ..extensions import login_manager, db, bcrypt, mail
from flask_mail import Message
from flask_principal import Permission, Identity, AnonymousIdentity, \
     identity_changed, identity_loaded, UserNeed, RoleNeed, ActionNeed
from app.emails import send_mail

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


# @auth_bp.before_request
# def before_request():
#     if (current_user.is_authenticated and
#             not current_user.confirm and
#             request.endpoint not in ['re_userconfirm', 'logout', 'user_confirm'] and
#             request.endpoint != 'static'):
#         flash('Hi, please activate your account first. Your endpoint:%s' % request.endpoint)
#         return render_template('unactivate.html')
#     session.modified = True


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
                current_user.confirm = True
                return redirect(url_for("admin.index"))
            else:
              error = "Ah-oh, your password is wrong."
        else:
            error = 'No exsting user.'
    return render_template("login.html", form=form, error=error)


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
            send_mail()
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
    next = request.args.get('next')
    # if not is_safe_url(next):
    #     return abort(400)
    return redirect(next or '/')

        
@auth_bp.route("/lost_and_find")
@fresh_login_required
def account_recovery():
    pass


@auth_bp.route('/re_userconfirm')
@login_required
def re_userconfirm():
    token = current_user.create_confirm_token()
    send_mail(sender='Your Mail@hotmail.com',
              recipients=['Your Mail@gmail.com'],
              subject='Activate your account',
              template='author/mail/welcome',
              mailtype='html',
              user=current_user,
              token=token)
    flash('Please Check Your Email..')
    return redirect(url_for('index'))


@auth_bp.route('/resetpassword', methods=['GET', 'POST'])
def reset_password():
    form = FormResetPasswordMail()
    if form.validate_on_submit():
        return 'RESET'
    return render_template('resetpassword.html', form=form)

