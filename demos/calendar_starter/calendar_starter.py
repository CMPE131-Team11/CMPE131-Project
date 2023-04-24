from pprint import pprint
from Google import Create_Service

client_file_path = 'credentials.json'
api_name = 'calendar'
version = 'v3'
scope = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(client_file_path, api_name, version, scope)
print(service)