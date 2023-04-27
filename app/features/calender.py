from datetime import datetime
from app.features.google_cred.Google import Create_Service
import json

class calendar_obj:
    secret_file = 'google_cred/credentials.json'
    api_name = 'calendar'
    api_version = 'v3'
    scope = ['https://www.googleapis.com/auth/calendar']
    event_body = {
        'summary' : 'Events'
    }
    def __init__(self):
        self.m_service = Create_Service(self.secret_file, self.api_name, self.api_version, self.scope)

    def add_event(self,p_event):
        self.m_service.events().insert(calendarId='primary', body = p_event.get_event()).execute()

class event:
    def __init__(self,p_name):
        self.m_name = p_name
        self.m_attendeelist = []
    
    def set_start_time(self, p_date, p_time, p_timezone = 'America/Los_Angeles'):
        rtc_date = datetime(p_date.m_year, p_date.m_month, p_date.m_day, p_time.m_hour, p_time.m_minute)
        self.m_start_time = {
            'dateTime': f'{rtc_date.isoformat()}',
            'timeZone': p_timezone,
        }

    def set_end_time(self, p_date, p_time, p_timezone = 'America/Los_Angeles'):
        rtc_date = datetime(p_date.m_year, p_date.m_month, p_date.m_day, p_time.m_hour, p_time.m_minute)
        self.m_end_time = {
            'dateTime': f'{rtc_date.isoformat()}',
            'timeZone': p_timezone,
        }

    def add_attendee(self, email):
        self.m_attendeelist.append({'email': email})

    def remove_attendee(self, email):
        self.m_attendeelist.remove({'email': email})

    def get_event(self):
        payload = {
          'summary': self.m_name,
          'description': 'This event was created by python',
          'start':self.m_start_time,
          'end': self.m_end_time,
          'attendees': self.m_attendeelist,
          
        }
        return payload



class date:
    def __init__(self, p_year, p_month, p_day):
        self.m_year = p_year
        self.m_month = p_month
        self.m_day = p_day

class time:
    def __init__(self, p_hour, p_minute=0):
        self.m_hour = p_hour
        self.m_minute = p_minute