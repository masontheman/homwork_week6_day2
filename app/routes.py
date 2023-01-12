from app import app 
from flask import render_template, redirect, url_for, flash
from app.forms import SignInForm
from app.models import User

@app.route('/')
def HomePage():
    return (render_template('homepage.html'))
@app.route('/signup',methods=["GET", "POST"])
def SecondPage():
    form = SignInForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        f = form.fname.data
        l = form.lname.data
        new_user = User(fname=f,lname=l,email=email,username=username,password=password)
        flash('Sign in successful')
        return redirect(url_for('HomePage'))
    return (render_template('secondpage.html',form=form))