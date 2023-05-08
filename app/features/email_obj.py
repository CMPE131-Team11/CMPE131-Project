import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError
import os
import pickle
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
    def get_emails(self, search_string):
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', ['https://www.googleapis.com/auth/gmail.readonly'])
        creds = flow.run_local_server(port=0)
        service = googleapiclient.discovery.build('gmail', 'v1', credentials=creds)
        user_id = 'me'  # 'me' refers to the authenticated user

        results = service.users().messages().list(userId=user_id, maxResults = 10, q=search_string).execute()  # this is where you can change the amount of emails to be printed --- maxResults=1 
        return results.get('messages', [])
 
    def search_email(self, search_string):
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', ['https://www.googleapis.com/auth/gmail.readonly'])
        creds = flow.run_local_server(port=0)
        service = googleapiclient.discovery.build('gmail', 'v1', credentials=creds)
        user_id = 'me'  # 'me' refers to the authenticated user

        results = service.users().messages().list(userId=user_id, maxResults=1, q=search_string).execute()  # this is where you can change the amount of emails to be printed --- maxResults=1 
        return results.get('messages', [])
