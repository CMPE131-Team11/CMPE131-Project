import pickle 
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class tasks:

    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/tasks']
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
            
        self.service = build('tasks', 'v1', credentials=self.creds)

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

<<<<<<< HEAD

    def add_task(self, task_title, task_list_name):
        tasklist_id = ''
        results = self.service.tasklists().list().execute()
=======
    def add_task(self, task_title, task_list_name):
        results = self.service.tasklists().list().execute()
        tasklist_id = ''
>>>>>>> adaf917 (class session)
        for item in results['items']:
            if item['kind'] == 'tasks#taskList' and item['title'] == task_list_name:
                tasklist_id = item['id']
    
        task_details = {
            "kind": "tasks#task",
            "title": str(task_title),
        }

        self.service.tasks().insert(tasklist=tasklist_id, body=task_details).execute()
<<<<<<< HEAD
    
def main():
    obj = tasks()
    obj.insert_tasklist("tasklist 2")
    obj.add_task("adding task to tasklist 2", "tasklist 2")
    obj.list_tasks()

main()
=======
>>>>>>> adaf917 (class session)
