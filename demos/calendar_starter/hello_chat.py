from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class spaces:
    def list_spaces(self):
        # Specify required scopes.
        SCOPES = ['https://www.googleapis.com/auth/chat.bot']

        # Specify service account details.
        CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name('/Users/kerryliu/Desktop/CMPE131/CMPE131-Project/demos/calendar_starter/token files/service_account.json', SCOPES)
        self.service = build('chat', 'v1', http=CREDENTIALS.authorize(Http()))
        space = self.service.spaces().list().execute()
        if not space:
            print("no space found")
        else:
            return space

s = spaces()
r = s.list_spaces()
print(r)

'''
# Specify required scopes.
SCOPES = ['https://www.googleapis.com/auth/chat.bot']

# Specify service account details.
CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name(
    'service_account.json', SCOPES)

# Build the URI and authenticate with the service account.
chat = build('chat', 'v1', http=CREDENTIALS.authorize(Http()))

# Create a Chat message.
result = chat.spaces().messages().create(

    # The space to create the message in.
    #
    # Replace SPACE with a space name.
    # Obtain the space name from the spaces resource of Chat API,
    # or from a space's URL.
    parent='spaces/SPACE',

    # The message to create.
    body={'text': 'Hello, world!'}

).execute()

print(result)
'''