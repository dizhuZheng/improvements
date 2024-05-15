from wtforms import fields
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo, InputRequired
from flask_ckeditor import CKEditorField
from .models import User
from flask_login import current_user


class LoginForm(FlaskForm):
    name = fields.StringField(label='name', validators=[DataRequired()])
    password = fields.PasswordField(label='password', validators=[DataRequired()])
    remember = fields.BooleanField(label='Remember me', default="checked")
    submit = fields.SubmitField('Submit')


class RegisterForm(FlaskForm):
    name = fields.StringField(label='name', validators=[DataRequired(), Length(3, 40)])
    password = fields.PasswordField(label='password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = fields.PasswordField('Repeat Password')
    email = fields.EmailField(label='email', validators=[DataRequired()])
    submit = fields.SubmitField('Submit')


def validate_email(form, email):
     if User.query.filter_by(email=email.data).first() and email.data == current_user.email:
          raise ValidationError('Please use a different email!')
    
def validate_name(form, name):
    if User.query.filter_by(name=name.data).first() and name.data == current_user.name:
        raise ValidationError('Please use a different name!')
    
def validate_password(form, password):
    if User.query.filter_by(password_hash=password.data).first() and password.data == current_user.password_hash:
        raise ValidationError('Please use a different password!')

class SettingForm(FlaskForm):
    name = fields.StringField(validators=[DataRequired(message = 'Enter a valid name'), Length(1, 30), validate_name])
    email = fields.EmailField(validators=[DataRequired(message = 'Enter a valid email'), Length(1, 60), validate_email])
    password = fields.StringField(validators=[InputRequired(), Length(1, 100), validate_password])
    about = CKEditorField('About Page')
    submit = fields.SubmitField('Update')


