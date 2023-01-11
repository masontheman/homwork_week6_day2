from app import app 
from flask import render_template, redirect, url_for, flash
from app.forms import SignInForm

@app.route('/')
def HomePage():
    return (render_template('homepage.html'))
@app.route('/signup',methods=["GET", "POST"])
def SecondPage():
    form = SignInForm()
    if form.validate_on_submit():
        flash('Sign in successful')
        return redirect(url_for('HomePage'))
    return (render_template('secondpage.html',form=form))