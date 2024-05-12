from wtforms import fields
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, ValidationError

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


class DemoForm(FlaskForm):
    title = fields.StringField(label='title', validators=[DataRequired(), Length(3, 40)])
    year = fields.TimeField(label='year', validators=[DataRequired(), Length(3, 40)])
    submit = fields.SubmitField('Submit')
