from googleapiclient.discovery import build
from google.oauth2 import service_account
import json
import click

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

@click.command()
@click.option("--name", prompt = "Enter your name:")
@click.option("--email", prompt = "Enter your email:")
@click.option("--role", prompt = "Enetr your role:")
@click.option("--expertise", prompt = "Enetr your expertise:")
@click.option("--mentor_id", prompt = "Enetr your mentor id:")
@click.option("--mentor_email", prompt = "Enetr your mentor email:")
@click.option("--mentee_id", prompt = "Enetr your mentee id:")
@click.option("--time", prompt = "Enetr the time of the meeting:")
@click.option("--status", prompt = "Enetr the status of the meeting:")
@click.option("--resource_id", prompt = "What is the resource id:")
@click.option("--topic", prompt = "Enter the topic of the meeting:")
@click.option("--date_requested", prompt = "Enter the date of request:")

def prompts(name, email, role, expertise, mentor_id, mentor_email, mentee_id, time, status, resource_id, topic, date_requested):
	user_id = {"Name": name,
		    "Email": email,
		    "Role": role,
		    "Expertise": expertise}

	meeting_id ={
	    "mentor_id": mentor_id,
	    "mentor_email": mentor_email,
	    "mentee_id": mentee_id,
	    "time": time,
	    "status": status
	}

	workshop_id ={
	    "resource_id": "",
	    "topic": "",
	    "date_requested": ""
	} 
	return user_id, meeting_id, workshop_id
	
if __name__ == '__main__':
	user_id, meeting_id, workshop_id = prompts()
	print(f"User ID: {user_id}")
	print(f"Meeting ID: {meeting_id}")
	print(f"Workshop ID: {workshop_id}")