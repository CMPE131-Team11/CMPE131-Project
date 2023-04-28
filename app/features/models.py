from flask_sqlalchemy import SQLAlchemy
from app import login,db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
class user(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(100),nullable=False,unique = True)
    password = db.Column(db.String(100),nullable = False)
    emails = db.relationship('Email',backref = 'user',lazy = True)
    #def __init__(self,username,password):
    #self.username = username
        #does not need self.password here
        #self.password = password
    #need check_password()
    def check_password(self, password):
        return check_password_hash(self.password, password)
    #need ser_password() in sign-up/
    # handles setting up password for new users
    def set_password(self, password):
        self.password = generate_password_hash(password)

    #need sign_up_()
class Email(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    sender_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable = False)
    recipient = db.Column(db.String(100),nullable = False)
    subject  = db.Column(db.String(100),nullable = False)
    body = db.Column(db.Text,nullable = False)
    emailType = db.Column(db.String(100),nullable = False)

    def __init__(self,sender_id,recipient,subject,body):
        self.sender_id = sender_id
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.emailType = "Inbox"

@login.user_loader
def load_user(id):
    return user.query.get(int(id))