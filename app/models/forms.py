#from flask_wtf import Form
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
#from wtforms.validators import DataRequired
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired])
    remember_me = BooleanField('remember_me', validators=[])
    submitted = SubmitField('Login')

 