from wtforms import fields
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, ValidationError, Email, Optional, URL
from flask_ckeditor import CKEditorField
from .models import Category


class PostForm(FlaskForm):
    title = fields.StringField('Title', validators=[DataRequired(), Length(1, 60)])
    category = fields.SelectField('Category', coerce=int, default=1)
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = fields.SubmitField()

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.category.choices = [(category.id, category.name)
                                 for category in Category.query.order_by(Category.name).all()]


class CategoryForm(FlaskForm):
    name = fields.StringField('Name', validators=[DataRequired(), Length(1, 30)])
    submit = fields.SubmitField()

    def validate_name(self, field):
        if Category.query.filter_by(name=field.data).first():
            raise ValidationError('Name already in use.')


class CommentForm(FlaskForm):
    author = fields.StringField('Name', validators=[DataRequired(), Length(1, 30)])
    email = fields.StringField('Email', validators=[DataRequired(), Email(), Length(1, 254)])
    site = fields.StringField('Site', validators=[Optional(), URL(), Length(0, 255)])
    body = fields.TextAreaField('Comment', validators=[DataRequired()])
    submit = fields.SubmitField()

