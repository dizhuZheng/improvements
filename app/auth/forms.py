from wtforms import fields
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, ValidationError
from ..extensions import db
from .models import User

class LoginForm(FlaskForm):
    name = fields.StringField(label='name', validators=[DataRequired()])
    password = fields.PasswordField(label='password', validators=[DataRequired()])
    submit = fields.SubmitField('Submit')


class RegisterForm(FlaskForm):
    name = fields.StringField(label='name', validators=[DataRequired(), Length(4, 40)])
    password = fields.PasswordField(label='password', validators=[DataRequired()])
    email = fields.StringField(label='email', validators=[DataRequired()])
    submit = fields.SubmitField('Submit')

    def validate_login(self):
        if db.session.query(User).filter_by(name=self.name.data).count() > 0:
            raise ValidationError('Duplicate username')
