from flask_sqlalchemy import SQLAlchemy
from app import login,db
from flask_login import UserMixin

class user(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(100),nullable=False,unique = True)
    password = db.Column(db.String(100),nullable = False)
    emails = db.relationship('Email',backref = 'user',lazy = True)
    def __init__(self,username,password):
        self.username = username
        self.password = password
class Email(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    #sender_id = db.Column(db.Integer,db.ForeignKey('user_id'),nullable = False)
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