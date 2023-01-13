from app import app, login_manager, db
from flask import render_template, redirect, url_for, flash
from app.forms import SignInForm, LogIn, CreateAddress,EditAddress,DeleteForm
from app.models import User, Address
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash
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

@app.route('/login',methods=["GET", "POST"])
def login():
    form = LogIn()
    if form.validate_on_submit():
        username = form.username.data 
        password = form.password.data
        user = User.query.filter_by(username = username).first()
        if user.check_password(password):
            login_user(user)
            flash('Log in successful')
            return redirect(url_for('HomePage'))
    return (render_template('login.html',form = form))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('HomePage'))

@app.route('/createaddress',methods=["GET", "POST"])
@login_required
def createaddress():
    form = CreateAddress()
    if form.validate_on_submit():
        f = form.first_name.data
        l = form.last_name.data
        p = form.phone_number.data
        a = form.address.data
        newaddress = Address(first_name=f,
        last_name = l, phone_number =p,
        address = a, user_id = current_user.id)
        flash('created the p#')
        return redirect(url_for('profiles'))
    return render_template('createaddress.html',form = form)

@app.route('/profile',methods=["GET", "POST"])
@login_required
def profiles():
    # userposts = Address.get(user_id = current_user.id)
    userposts = db.session.execute(db.select(Address).filter_by(user_id=current_user.id)).scalars()
    return render_template('profile.html',userposts = userposts)

@app.route('/profile/edit/<int:post_id>',methods=["GET", "POST"])
@login_required
def editaddress(post_id):
    userposts = db.session.execute(db.select(Address).filter_by(id=post_id)).scalar_one()
    form = EditAddress()
    if form.validate_on_submit():
        f = form.first_name.data
        l = form.last_name.data
        p = form.phone_number.data
        a = form.address.data
        if p:
            userposts.phone_number = p
            db.session.commit()
        if a:
            userposts.address = a
            db.session.commit()
        if f:
            userposts.first_name = f
            db.session.commit()
        if l:
            userposts.last_name = l
            db.session.commit()
        return redirect(url_for('profiles'))
    return  render_template('editaddress.html', form = form)

@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    flash('sign in to create addrsses')
    return redirect(url_for('HomePage'))

@app.route('/profile/delete/<int:post_id>',methods=["GET", "POST"])
@login_required
def deleteaddress(post_id):
    userposts = db.session.execute(db.select(Address).filter_by(id=post_id)).scalar_one()
    userposts.deleteaddress()
    return redirect(url_for('profiles'))

