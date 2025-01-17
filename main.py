import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate(r"./Firbase\ key/skillsink-9567a-firebase-adminsdk-fbsvc-2e87c26293.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

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

workshop_id = {
    "resource_id": "",
    "topic": "",
    "date_requested": ""
}