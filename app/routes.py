import app.features.email_obj
import app.features.tasks
import app.features.calender
import app.features.tasks
from app.features.models import user, Email
from app.features.forms import login_form, sign_up_form
from flask import session, request, flash, redirect, render_template, url_for
from flask_login import login_user, logout_user, fresh_login_required, current_user
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
    # class in form.py
    form = login_form()
    # submit into the form
    if form.validate_on_submit():
        print("here\n\n")
        #site_user is check if user is already in the form
        site_user = user.query.filter_by(username=form.username.data).first()
        
        if site_user and site_user.check_password(form.password.data) == True:
            login_user(site_user)
            #return redirect("/")
            return render_template('test.html', form=form)
        else:
            flash("Please register for an account.")
            return render_template('login.html', form=form)
    return render_template('login.html', form=form)

#don't have yet
@myapp_obj.route("/logout/")
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect('/login/')

@myapp_obj.route("/sign_up/",methods = ['POST', 'GET'])
def sign_up():
    # from forms.py
    form = sign_up_form()
    if form.validate_on_submit():
        existing_user = user.query.filter_by(username=form.username.data).first()
        if existing_user == None:
            # create new user
            new_user = user(username = form.username.data)
            # pass into set_password()
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("login"))
        else:
            flash("User name is already registered.")
    return render_template('signup.html', form=form)
    

@myapp_obj.route("/deactivate/", methods = ['POST', 'GET'])
def delete_account():
    account = user.query.filter(user.id == current_user.id).first()
    db.session.delete(account)
    db.session.commit()
    flash("Your account has been deactivated.")
    return redirect(url_for('login'))

@myapp_obj.route("/edit_profile", methods = ['POST'])
def edit_user_profile():
    user_id = session.get('user_id')
    if user_id:
        curr_user = user.query.get(user_id)
        curr_user.username = request.form['username']
        curr_user.password = request.form['password']
        db.session.commit()
    return
    