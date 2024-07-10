from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

# Login Form
class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    password = PasswordField('password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
    submit = SubmitField('login')

# Signup Form
class SignupForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    password = PasswordField('password', validators=[DataRequired(), Length(min=8)], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField('signup')