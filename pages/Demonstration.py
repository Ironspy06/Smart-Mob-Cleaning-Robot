import streamlit as st
import cv2
import numpy as np
import pyrebase

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

firebase=pyrebase.initialize_app(config)

db=firebase.database()

st.title("DEMONSTRATION")

st.subheader("SNAKE MOVEMENT")
video_file = open('video1.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

st.subheader("EDGE DETECTION")
video_file = open('video2.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

st.subheader("CHANGE MOVEMENT")

def snake():
   
   data={"Model":"Snake"}
   print("hi")
   db.child("Motion").update(data)
def random():
   data={"Model":"Random"}
   print("hilo")
   db.child("Motion").update(data)


st.subheader("CAMERA INPUT")

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # Check the type of cv2_img:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(cv2_img))

    # Check the shape of cv2_img:
    # Should output shape: (height, width, channels)
    st.write(cv2_img.shape)