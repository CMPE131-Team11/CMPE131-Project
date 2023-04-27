import features.email
import features.tasks
import features.calender
import features.tasks
from flask import session,request
from models import db, User, Email
from app import myapp_obj

@app.before_first_request
def create_tables():
    db.create_all()

@myapp_obj.route("/addToSpam",methods = ['POST'])
def addToSpam():
    email_id = request.form['email_id']
    if email_id:
        email = Email.query.get(email_id)
        email.emailType = 'SPAM'
        db.session.commit()


@myapp_obj.route("/spam/")
def showSpam():
    spamList = Emails.query.filter(emailType = 'SPAM', recipient = session.get('username'))
    return spamList

@myapp_obj.route("/edit_profile", methods = ['POST'])
def editUserProfile():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.get(user_id)
        user.username = request.form['username']
        user.password = request.form['password']
        db.session.commit()
    return
    