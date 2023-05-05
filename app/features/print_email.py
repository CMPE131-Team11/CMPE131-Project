import os
import pickle
import base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import googleapiclient.discovery
from email import message_from_bytes

def get_credentials():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', ['https://www.googleapis.com/auth/gmail.readonly'])
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

def get_email_messages(service, user_id, email_id):
    email_data = service.users().messages().get(userId=user_id, id=email_id, format='raw').execute()
    email_content = base64.urlsafe_b64decode(email_data['raw'].encode('ASCII'))
    return email_content

def print_the_email():
    creds = get_credentials()
    service = googleapiclient.discovery.build('gmail', 'v1', credentials=creds)
    user_id = 'me'  # 'me' refers to the authenticated user

    results = service.users().messages().list(userId=user_id, maxResults=1).execute()  # this is where you can change the amount of emails to be printed --- maxResults=1 
    messages = results.get('messages', [])

    for message in messages:
        email_id = message['id']
        email_content = get_email_messages(service, user_id, email_id)
        email_message = message_from_bytes(email_content)

        print(f"Subject: {email_message['subject']}")
        print(f"From: {email_message['from']}")
        print(f"To: {email_message['to']}")
        print("Body:")

        for part in email_message.walk():
            if part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
                print(body.decode('utf-8'))
        print("\n---\n")

#if __name__ == '__main__':
  # main()                