from flask import current_app, Blueprint, render_template, redirect, url_for, request
# from jinja2 import TemplateNotFound
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('blog.index'))

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        admin = Admin.query.first()
        if admin:
            if username == admin.username and admin.validate_password(password):
                login_user(admin, remember)
                flash('Welcome back.', 'info')
                return redirect_back()
            flash('Invalid username or password.', 'warning')
        else:
            flash('No account.', 'warning')
    return render_template('auth/login.html', form=form)


@auth_bp.route('/signup')
def signup():
    return render_template('signup.html')


@auth_bp.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO books (title, author, pages_num, review)'
                'VALUES (%s, %s, %s, %s)',
                (title, author, pages_num, review))
    conn.commit()
    cur.close()
    conn.close()
    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return 'it is wrong'
    
    # conn = get_db_connection()
    #     cur = conn.cursor()
    #     cur.execute('INSERT INTO books (title, author, pages_num, review)'
    #                 'VALUES (%s, %s, %s, %s)',
    #                 (title, author, pages_num, review))
    #     conn.commit()
    #     cur.close()
    #     conn.close()
        return redirect(url_for('index'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))


@auth_bp.route('/logout')
def logout():
    return 'log out'