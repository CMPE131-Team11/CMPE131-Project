from datetime import datetime
from app.features.google_cred.Google import Create_Service
import json

class calendar_obj:
    secret_file = 'credentials.json'
    api_name = 'calendar'
    api_version = 'v3'
    scope = ['https://www.googleapis.com/auth/calendar']
    event_body = {
        'summary' : 'Events'
    }
    def __init__(self, goog):
        self.m_service = goog
        
    def add_event(self,p_event):
        self.m_service.events().insert(calendarId='primary', body = p_event.get_event()).execute()

class event:
    def __init__(self,p_name):
        self.m_name = p_name
        self.m_attendeelist = []
        self.m_description = "This "
    
    def set_start_time(self, p_datetime, p_timezone = 'America/Los_Angeles'):
        rtc_date = datetime(p_datetime.year, p_datetime.month, p_datetime.day, p_datetime.hour, p_datetime.minute)
        self.m_start_time = {
            'dateTime': f'{rtc_date.isoformat()}',
            'timeZone': p_timezone,
        }

    def set_end_time(self, p_datetime, p_timezone = 'America/Los_Angeles'):
        rtc_date = datetime(p_datetime.year, p_datetime.month, p_datetime.day, p_datetime.hour, p_datetime.minute)
        self.m_end_time = {
            'dateTime': f'{rtc_date.isoformat()}',
            'timeZone': p_timezone,
        }

    def add_description(self, p_description):
        self.m_description = p_description

    def add_attendee(self, email):
        self.m_attendeelist.append({'email': email})


    def remove_attendee(self, email):
        self.m_attendeelist.remove({'email': email})

    def get_event(self):
        payload = {
          'summary': self.m_name,
          'description': self.m_description,
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