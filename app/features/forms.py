from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DateTimeLocalField
from wtforms.validators import DataRequired, Email

class login_form(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class create_tasks_form(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    title = StringField('Task List', validators=[DataRequired()])
    task_subject = StringField('Task', validators=[DataRequired()])
    submit = SubmitField('Add')

class sign_up_form(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class edit_profile_form(FlaskForm):
    new_username = StringField('Username', validators=[DataRequired()])
    new_password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Edit')

class send_email_form(FlaskForm):
    recipient = StringField('Recipient', validators = [DataRequired()])
    subject = TextAreaField('Subject', validators = [DataRequired()])
    body = TextAreaField('Body', validators = [DataRequired()])
    submit = SubmitField('Send')

class create_event_form(FlaskForm):
    start_time = DateTimeLocalField('Start Time', validators = [DataRequired()], format='%Y-%m-%dT%H:%M')
    end_time = DateTimeLocalField('End Time', validators = [DataRequired()], format='%Y-%m-%dT%H:%M')
    title = TextAreaField('Title', validators = [DataRequired()])
    description = TextAreaField('Description')
    attendees = TextAreaField('Attendees', validators = [DataRequired()])
    submit = SubmitField('Send')
