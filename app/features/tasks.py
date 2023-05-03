import pickle 
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class tasks:

    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/tasks']
        self.service = None
    def submit(self, creds):
        self.service = build('tasks', 'v1', credentials=self.creds)

    def get_cred(self, email):
        self.creds = None
        if os.path.exists('token_calendar_v3.pickle'):
            with open('token_calendar_v3.pickle', 'rb') as token:
                self.creds = pickle.load(token)
            
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', 'https://www.googleapis.com/auth/tasks')
                self.creds = flow.run_local_server(port=0)
            
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)
        return self.creds
            
    def list_tasks(self):
        results = self.service.tasklists().list().execute()
        items = results.get('item', [])
        return items
    
    def insert_tasklist(self, p_name):
        tasklist_details = {
            "kind": "tasks#taskList",
            "title": str(p_name),
        }

        self.service.tasklists().insert(body=tasklist_details).execute()

    def add_task(self, task_title, task_list_name):
        results = self.service.tasklists().list().execute()
        tasklist_id = ''
        for item in results['items']:
            if item['kind'] == 'tasks#taskList' and item['title'] == task_list_name:
                tasklist_id = item['id']
    
        task_details = {
            "kind": "tasks#task",
            "title": str(task_title),
        }

        self.service.tasks().insert(tasklist=tasklist_id, body=task_details).execute()

