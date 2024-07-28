from flask import render_template, redirect, request, url_for, flash, session
from .forms import LoginForm, SignupForm
from . import auth
from ..db_functions import create_user, login_user, get_user

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Display login form
    form = LoginForm()
    if form.validate_on_submit():
        res = login_user(form.email.data, form.password.data)
        if res is not False:
            user = get_user(res)
            session['user'] = user  # Store user in session
            return redirect(url_for('main.index'))
        else:
            flash("Invalid email or password.")
        
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