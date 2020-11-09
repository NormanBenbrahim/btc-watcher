import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os 

project_id = os.getenv('PROJECT_ID')

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {"projectId": project_id})

db = firestore.client()