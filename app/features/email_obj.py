import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from requests import HTTPError

class Send_email:

    def add_recipient(self, p_recipient):
        self.m_recipient = p_recipient

    def set_body_text(self, p_body):
        self.m_body = p_body

    def set_subject_text(self, p_subject):
        self.m_subject = p_subject

    def send(self):
        SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
        flow = InstalledAppFlow.from_client_secrets_file('google_cred/credentials.json', SCOPES)
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
