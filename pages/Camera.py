import streamlit as st
import pyrebase
from PIL import Image
import math
import time
# Initialize Firebase app with credentials
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
db = firebase.database()

size = (80, 80)
flag=-1
# Create a Streamlit placeholder for the image
image_placeholder = st.empty()

# Initialize placeholder for distance
# text_placeholder6 = st.empty()

# # Initialize variables for calculating distance
# velocity = 0.0
# position = 0.0
# last_updated = 0
# time_diff = 0.0

# def calculate_distance(velocity, position, time_diff, x, y, z):
#     # Convert accelerometer data to acceleration in m/s^2
#     acceleration = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    
#     # Update velocity and position based on acceleration
#     velocity = velocity + acceleration * time_diff
#     position = position + velocity * time_diff
    
#     # Return distance
#     return position

# Main loop
while True:

    video_url = db.child("Motion").child("Image").get().val()

      # Display video in Streamlit app

    image_placeholder.image(video_url)

    # # Get accelerometer data from Firebase
    # x = db.child('Motion').child('Accelerometer').child("0").get().val()
    # y = db.child('Motion').child('Accelerometer').child("1").get().val()
    # z = db.child('Motion').child('Accelerometer').child("2").get().val()
    # current_updated = db.child('Motion').child('Accelerometer').child("time").get().val()

    # # Calculate time difference
    # if last_updated is not None and current_updated is not None:
    #     time_diff = (current_updated - last_updated) / 1000.0

    # # Calculate distance if accelerometer data has been updated
    # if current_updated is not None and last_updated is not None and current_updated > last_updated:
    #     # Calculate distance using accelerometer data
    #     distance = calculate_distance(velocity, position, time_diff, x, y, z)
    #     print(distance)  # Debugging statement
        
    #     # Update placeholder with distance value
    #     text_placeholder6.text(f"Distance: {distance:.2f} m")
        
    #     # Update last_updated
    #     last_updated = current_updated
    
    # # Wait for 100 milliseconds before getting new data
    # time.sleep(0.1)