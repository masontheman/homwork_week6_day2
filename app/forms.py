from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileRequired
from wtforms import EmailField,SubmitField,PasswordField,FormField,StringField
from wtforms.validators import DataRequired, EqualTo, InputRequired

class SignInForm(FlaskForm):
    fname = StringField('First Nane',validators=[InputRequired()])
    lname = StringField('Last Name',validators=[InputRequired()])
    email = EmailField('Email',validators=[InputRequired()])
    username = StringField('Username',validators=[InputRequired()])
    password = PasswordField('Password',validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[InputRequired(),EqualTo('password')])
    submit = SubmitField()


