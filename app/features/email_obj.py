import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError
import os
import pickle
from bs4 import BeautifulSoup
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import googleapiclient.discovery
from email import message_from_bytes

class Send_email:

    def add_recipient(self, p_recipient):
        self.m_recipient = p_recipient

    def set_body_text(self, p_body):
        self.m_body = p_body

    def set_subject_text(self, p_subject):
        self.m_subject = p_subject

    def send(self):
        SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        service = build('gmail', 'v1', credentials=creds)
        message = MIMEText(self.m_body)
        message['to'] = self.m_recipient
        message['subject'] = self.m_subject
        create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

        try:
            message = (service.users().messages().send(userId="me", body=create_message).execute())
            print(F'sent message to {message} Message Id: {message["id"]}')
        except HTTPError as error:
            print(F'An error occurred: {error}')
            message = None

class print_email:
    def __init__(self):
        self.creds = None
        if os.path.exists("token.pickle"):
            with open("token.pickle", "rb") as token:
                self.creds = pickle.load(token)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                self.flow = InstalledAppFlow.from_client_secrets_file('credentials.json', ['https://mail.google.com/'])
                self.creds = self.flow.run_local_server(port=0)
            # save the credentials for the next run
            with open("token.pickle", "wb") as token:
                pickle.dump(self.creds, token)
        self.service = googleapiclient.discovery.build('gmail', 'v1', credentials=self.creds)
        self.user_id = 'me'  # 'me' refers to the authenticated user

    def get_emails(self):
        results = self.service.users().messages().list(userId=self.user_id, maxResults = 10).execute()  # this is where you can change the amount of emails to be printed --- maxResults=1 
        messages = results.get('messages', [])
        emails = []
        for message in messages:
            email_id = message['id']
            email_data = self.service.users().messages().get(userId=self.user_id, id=email_id, format='raw').execute()
            email_content = base64.urlsafe_b64decode(email_data['raw'].encode('ASCII'))
            email_message = message_from_bytes(email_content)
            for part in email_message.walk():
                if part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=True)
            soup = BeautifulSoup(body, features="html.parser")
            body = soup.get_text()
            try: 
                a = email_obj(message['id'], email_message['subject'], email_message['from'], email_message['to'], body)
                emails.append(a)
            except:
                pass
        return emails
 
    def search_email(self, search_string):
        results = self.service.users().messages().list(userId=self.user_id, maxResults=10, q=search_string).execute()  # this is where you can change the amount of emails to be printed --- maxResults=1 
        messages = results.get('messages', [])
        emails = []
        for message in messages:
            email_id = message['id']
            email_data = self.service.users().messages().get(userId=self.user_id, id=email_id, format='raw').execute()
            email_content = base64.urlsafe_b64decode(email_data['raw'].encode('ASCII'))
            email_message = message_from_bytes(email_content)
            for part in email_message.walk():
                if part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=True)
            soup = BeautifulSoup(body, features="html.parser")
            body = soup.get_text()
            try: 
                a = email_obj(message['id'], email_message['subject'], email_message['from'], email_message['to'], body)
                emails.append(a)
            except:
                pass
        return emails
    
    def delete_email(self, p_id):
        self.service.users().messages().delete(userId='me', id=p_id).execute()
    
class email_obj():
    def __init__(self, p_id, p_subject, p_sender, p_to, p_body):
        self.m_id = p_id
        self.m_subject = p_subject
        self.m_sender = p_sender
        self.m_to = p_to
        self.m_body = p_body
