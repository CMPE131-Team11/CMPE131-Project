from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class login_form(FlaskForm):
    username = StringField('Userename', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class create_tasks_form(FlaskForm):
    username = StringField('Userename', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    task_subject = StringField('Task', validators=[DataRequired()])
#     submit = SubmitField('Add')

class sign_up_form(FlaskForm):
    username = StringField('Userename', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class edit_profile_form(FlaskForm):
    new_username = StringField('Userename', validators=[DataRequired()])
    new_password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Edit')

class send_email_form(FlaskForm):
    recipient = StringField('Recipient', validators = [DataRequired()])
    subject = TextAreaField('Subject', validators = [DataRequired()])
    body = TextAreaField('Body', validators = [DataRequired()])
    submit = SubmitField('Send')

class create_event_form(FlaskForm):
    recipient = StringField('Recipient', validators = [DataRequired()])
    subject = TextAreaField('Subject', validators = [DataRequired()])
    body = TextAreaField('Body', validators = [DataRequired()])