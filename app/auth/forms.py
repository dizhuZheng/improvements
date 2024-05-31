from wtforms import fields
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo, InputRequired
from flask_ckeditor import CKEditorField
from .models import User
from flask_login import current_user
from ..extensions import bcrypt

class LoginForm(FlaskForm):
    name = fields.StringField(label='name or email', validators=[DataRequired()])
    password = fields.PasswordField(label='password', validators=[DataRequired()])
    remember = fields.BooleanField(label='Remember me', default="checked")
    submit = fields.SubmitField('Submit')


class RegisterForm(FlaskForm):
    name = fields.StringField(label='name', validators=[DataRequired(), Length(3, 40)])
    password = fields.PasswordField(label='password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = fields.PasswordField('Repeat Password')
    email = fields.EmailField(label='email', validators=[DataRequired()])
    submit = fields.SubmitField('Submit')


class FormResetPasswordMail(FlaskForm):
    email = fields.EmailField('Email', validators=[
        DataRequired(),Length(5, 30)
    ])
    submit = fields.SubmitField('Send Confirm EMAIL')


class ChangeNameForm(FlaskForm):
    name = fields.StringField(validators=[DataRequired(message = 'Enter a valid name'), Length(1, 20)])
    submit = fields.SubmitField('Submit')

    def validate_name(form, name):
        if name.data == current_user.name:
            raise ValidationError('You can\'t use your old name!')
        elif User.query.filter_by(name=name.data).first():
            raise ValidationError('Someone else is using this name!')


class ChangeEmailForm(FlaskForm):
    email = fields.EmailField(validators=[DataRequired(message = 'Enter a valid email'), Length(1, 50)])
    submit = fields.SubmitField('Submit')

    def validate_email(form, email):
        if email.data == current_user.email:
            raise ValidationError('You can\'t use your old email!')
        elif User.query.filter_by(email=email.data).first():
            raise ValidationError('Someone else is using this email!')


class ChangeAboutForm(FlaskForm):
    about = CKEditorField(validators=[DataRequired(message = 'Enter anything you like')])
    submit = fields.SubmitField('Submit')
