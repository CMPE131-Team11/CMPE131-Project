import app.features.email_obj
import app.features.tasks
import app.features.calender
import app.features.tasks
from app.features.models import user, Email
from app.features.forms import login_form
from flask import session, request, flash, redirect, render_template
from flask_login import login_user, logout_user, login_required
from app import myapp_obj, db

@myapp_obj.before_first_request
def create_db():
    db.create_all()
@myapp_obj.route("/addToSpam",methods = ['POST'])
def add_to_spam():
    email_id = request.form['email_id']
    if email_id:
        email = Email.query.get(email_id)
        email.emailType = 'SPAM'
        db.session.commit()

@myapp_obj.route("/login/", methods=['GET', 'POST'])
def login():
    form = login_form()
    if form.validate_on_submit():
        print("here\n\n")
        site_user = user.query.filter_by(username=form.username.data)
        if site_user and site_user.check_password(form.password.data):
            login_user(site_user)
            return redirect("/")
        else:
            return render_template('login.html', form=form)
    return render_template('login.html', form=form)

@myapp_obj.route("/logout/")
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect('/login/')

@myapp_obj.route("/sign_up/",methods = ['POST'])
def sign_up():
    form = sign_up()
    if form.validate_on_submit():
        new_user = user()
        new_user.username = form.username.data
        
    

@myapp_obj.route("/deactivate/")
def delete_accout():
    
    flash("Your account has been deactivated.")
    return 

@myapp_obj.route("/edit_profile", methods = ['POST'])
def edit_user_profile():
    user_id = session.get('user_id')
    if user_id:
        curr_user = user.query.get(user_id)
        curr_user.username = request.form['username']
        curr_user.password = request.form['password']
        db.session.commit()
    return
    