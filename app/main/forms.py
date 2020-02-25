from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField
from wtforms.validators import DataRequired

from app.main.routes import images


class ProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message="Name required")])
    img = FileField('Profile Image', validators=[FileRequired(message="File required"), FileAllowed(images, 'Images only!')])
