from flask_sqlalchemy import SQLAlchemy
from app import login,db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
class user(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(100),nullable=False,unique = True)
    password = db.Column(db.String(100),nullable = False)
    emails = db.relationship('Email',backref = 'user',lazy = True)
    def check_password(self, password):
        return check_password_hash(self.password, password)
    def set_password(self, password):
        self.password = generate_password_hash(password)

class Chat(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100),nullable=True)
    receiver_username = db.Column(db.String(100), nullable=True)
    message = db.Column(db.String(100), nullable=False)
    time_send = db.Column(db.DateTime, nullable=False)

    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))


@login.user_loader
def load_user(id):
    return user.query.get(int(id))