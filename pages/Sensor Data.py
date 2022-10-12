from gc import isenabled
import pyrebase
import random
import pandas as pd
import streamlit as st
import numpy as np
import time
import threading
import streamlit.components.v1 as components
import base64
from PIL import Image
# config= {
#   "apiKey": "AIzaSyBHiBLqMM4j7O1QsCsbt-kQYNCfduhPRSI",
#   "authDomain": "ultrasonic-ec709.firebaseapp.com",
#   "databaseURL": "https://ultrasonic-ec709-default-rtdb.firebaseio.com",
#   "projectId": "ultrasonic-ec709",
#   "storageBucket": "ultrasonic-ec709.appspot.com",
#   "messagingSenderId": "745166098162",
#   "appId": "1:745166098162:web:5901af8a8772cf3dd78a6b",
#   "measurementId": "G-CEFJHZJL05"
# }

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

# [theme]
# base="dark"
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: contain;
    background-position: center;
    background-attachment: scroll;
    background-repeat: no-repeat;
    position:fixed;
    height: auto;
    
    }

    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

#set_background("C:/Users/Pratik/OneDrive/Desktop/Project/robot.png")
set_background("C:/Users/Pratik/OneDrive/Desktop/Project/My project.jpg")

# st.title("SENSOR DATA")
# def snake():
   
#    data={"Model":"Snake"}
#    print("hi")
#    db.child("Motion").update(data)
# def random():
#    data={"Model":"Random"}
#    print("hilo")
#    db.child("Motion").update(data)

# s=st.button(label='Snake Movement',on_click=snake)
# r=st.button(label='Random Movement',on_click=random)


res=-1
res1="Hello"
check=-1
ans="a"
col1, col2, col3,col4= st.columns(4)
with col1:
        st.header("IR Data")
        
with col2:
        st.header("SONAR")   
with col3:
        st.header("Motion")    
with col4:
        st.header("Battery") 


while True:

    with col1:

        ir=db.child('Motion').child('IR').get()
        if ir.val()==1 and res1!="Edge Detected... Avoiding the edge":
            st.write("Edge Detected... Avoiding the edge")
            res1="Edge Detected... Avoiding the edge"
        elif ir.val()==0 and res1!="Edge not detected":
            st.write("Edge not detected")
            res1="Edge not detected"

    with col2:
        UltraSonic=db.child('Motion').child('US').get()
        
        if UltraSonic.val()!=res:
           st.write(UltraSonic.val())
           res=UltraSonic.val()


    with col3:        
        orient=db.child('Motion').child('Orientation').get()
        if orient.val()!=check:
    
            if orient.val()==0:
                st.write("Stop")
            elif orient.val()==1:
                st.write("Forward")
            elif orient.val()==2:
                st.write("Backward")
            elif orient.val()==3:
                st.write("Left")
            elif orient.val()==4:
                st.write("Right")

            check=orient.val()


    with col4:
        battery=db.child('Motion').child('Battery').get()
        battery1=battery.val()/11.1
        if battery1*100>70 and ans!="High":
            st.write("High")
            ans="High"
        elif battery1*100==50 and ans!="Medium":
            st.write("Medium")
            ans="Medium"
        elif battery1*100<=20 and ans!="Battery Low, Charge the battery":
            st.write("Battery Low, Charge the battery")
            ans="Battery Low, Charge the battery"


