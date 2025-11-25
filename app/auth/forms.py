from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length

class adminForm(FlaskForm):
    """Super admin form"""

    username = StringField('Username',validators=[DataRequired(message='Username is required!'),Length(min=3, max=40, message='Username must be between 3 and 40.')])

    password = PasswordField('Password',validators=[DataRequired(message='Password is required!')])

    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Login')