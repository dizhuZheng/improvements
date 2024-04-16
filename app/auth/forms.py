from wtforms import fields
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, ValidationError

class LoginForm(FlaskForm):
    name = fields.StringField(label='name', validators=[DataRequired()])
    password = fields.PasswordField(label='password', validators=[DataRequired()])
    submit = fields.SubmitField('Submit')


class RegisterForm(FlaskForm):
    name = fields.StringField(label='name', validators=[DataRequired(), Length(4, 40)])
    password = fields.PasswordField(label='password', validators=[DataRequired()])
    email = fields.StringField(label='email', validators=[DataRequired()])
    submit = fields.SubmitField('Submit')
