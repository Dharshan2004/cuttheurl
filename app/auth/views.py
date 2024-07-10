from flask import render_template, redirect, request, url_for, flash
from .forms import LoginForm, SignupForm
from . import auth
from ..db_functions import create_user

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Display login form
    form = LoginForm()
    if form.validate_on_submit():
        print(form.email.data)
        return "Logged in successfully."
    return render_template('auth/login.html', form=form)

@auth.route('/signup', methods=['GET', 'POST'])
def register():
    # Display registration form
    form = SignupForm()
    if form.validate_on_submit():
        res = create_user(form.email.data, form.password.data)
        if res:
            return "User created successfully."
        else:
            return "User already exists."
        
    return render_template('auth/signup.html', form=form)
    
@auth.route('/logout')
def logout():
    # Handle logout
    pass