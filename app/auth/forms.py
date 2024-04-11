from wtforms import fields, validators
from flask_wtf import FlaskForm, CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    login = fields.StringField(label=u'管理员账号', validators=[DataRequired()])
    password = fields.PasswordField(label=u'密码', validators=[DataRequired()])
    submit = fields.SubmitField('Submit')


    

    
