from wtforms import fields, validators
from flask_wtf import FlaskForm, CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    name = fields.StringField(label='name', validators=[DataRequired()])
    password = fields.PasswordField(label='password', validators=[DataRequired()])
    submit = fields.SubmitField('Submit')


    

    
