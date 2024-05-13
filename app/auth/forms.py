from wtforms import fields
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, ValidationError
from flask_ckeditor import CKEditorField


class LoginForm(FlaskForm):
    name = fields.StringField(label='name', validators=[DataRequired()])
    password = fields.PasswordField(label='password', validators=[DataRequired()])
    remember = fields.BooleanField(label='Remember me', default="checked")
    submit = fields.SubmitField('Submit')


class RegisterForm(FlaskForm):
    name = fields.StringField(label='name', validators=[DataRequired(), Length(3, 40)])
    password = fields.PasswordField(label='password', validators=[DataRequired()])
    email = fields.EmailField(label='email', validators=[DataRequired()])
    submit = fields.SubmitField('Submit')


class SettingForm(FlaskForm):
    name = fields.StringField('Name', validators=[DataRequired(), Length(1, 30)])
    email = fields.EmailField('Blog Title', validators=[DataRequired(), Length(1, 60)])
    password = fields.StringField('Blog Sub Title', validators=[DataRequired(), Length(1, 100)])
    about = CKEditorField('About Page', validators=[DataRequired()])
    submit = fields.SubmitField()
