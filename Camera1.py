import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# initialize Firebase Admin SDK
cred = credentials.Certificate('C:/Users/Pratik/Downloads/Robot.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://robot-68d4d-default-rtdb.firebaseio.com'
})

# initialize pyrebase
config = {
  "apiKey": "AIzaSyCjULZ1FxzQHvMji5OR-OZnyOxY9KwV_GA",
  "authDomain": "robot-68d4d.firebaseapp.com",
  "databaseURL": "https://robot-68d4d-default-rtdb.firebaseio.com",
  "projectId": "robot-68d4d",
  "storageBucket": "robot-68d4d.appspot.com",
  "messagingSenderId": "1071151697658",
  "appId": "1:1071151697658:web:635787e41378b95fa54343",
  "measurementId": "G-42522D1CWQ"
}
firebase = pyrebase.initialize_app(config)

# get video file path
video_file_path = 'C:/Users/Pratik/OneDrive/Desktop/CIR/Bala1.jpeg'

# upload video to Firebase Storage
storage = firebase.storage()
storage.child('images/' + video_file_path).put(video_file_path)

# get the download URL of the video
download_url = storage.child('images/' + video_file_path).get_url(None)

# save the download URL to Realtime Database
ref = db.reference('images')
video_ref = ref.child('My_image')
video_ref.set({
    'title': 'My image',
    'url': download_url
})
