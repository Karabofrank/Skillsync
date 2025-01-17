from googleapiclient.discovery import build
from google.oauth2 import service_account
import json

scopes = ["https://www.googleapis.com/auth/calendar", "https://www.googleapis.com/auth/calendar.events"]
sa_file = 'service-account.json'
zone = 'us-central1-a'
project_id = "skillsync-448109"

credentials = service_account.Credentials.from_service_account_file(sa_file, scopes=scopes)

service = build('calendar','v3', credentials=credentials)

request = service.calendarList().list().execute()

def get_user_token(email):
    # I need the database
        return None
    
print(json.dumps(request, sort_keys=True, indent=4))
# User ID dictionary
user_id = {"Name": "",
           "Email": "",
           "Role": "",
           "Expertise": ""}

meeting_id ={
    "mentor_id": "",
    "mentor_email": "",
    "mentee_id": "",
    "time": "",
    "status": ""
}

workshop_id ={
    "resource_id": "",
    "topic": "",
    "date_requested": ""
}