import app.features.email_obj
import features.tasks
import features.calender
import features.tasks
from flask import session,request
from models import db, User, Email
from app import myapp_obj

@myapp_obj.before_first_request
def create_tables():
    db.create_all()

@myapp_obj.route("/addToSpam",methods = ['POST'])
def add_to_spam():
    email_id = request.form['email_id']
    if email_id:
        email = Email.query.get(email_id)
        email.emailType = 'SPAM'
        db.session.commit()


@myapp_obj.route("/spam/")
def show_spam():
    spamList = Emails.query.filter(emailType = 'SPAM', recipient = session.get('username'))
    return spamList

@myapp_obj.route("/edit_profile", methods = ['POST'])
def edit_user_profile():
    user_id = session.get('user_id')
    if user_id:
        curr_user = user.query.get(user_id)
        curr_user.username = request.form['username']
        curr_user.password = request.form['password']
        db.session.commit()
    return
    