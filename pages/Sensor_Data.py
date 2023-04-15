from gc import isenabled
import pyrebase
import streamlit as st
import time
import math
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
res=-1
res1="Hello"
check=-1
check2=-1
ans="a"

col1, col2, col3,col4,col5= st.columns([4,3,3,3,3])
with col1:
        st.header("Edge")
        text_placeholder1 = st.empty() 
with col2:
        st.header("Distance") 
        text_placeholder2 = st.empty() 
with col3:
        st.header("Motion")
        text_placeholder3 = st.empty()  
with col4:
        st.header("Obstacle")  
        text_placeholder4 = st.empty()
with col5:
        st.header("Battery") 
        text_placeholder5 = st.empty()

# with col6:
#          st.header("Area")
#          text_placeholder6= st.empty()
while True:

    with col1:

        ir=db.child('Motion').child('Edge').get()
        if ir.val()==1 and res1!="Edge Detected... Avoiding the edge":
            text_placeholder1.text("Edge Detected... Avoiding the edge")
            res1="Edge Detected... Avoiding the edge"
        elif ir.val()==0 and res1!="Edge not detected":
            text_placeholder1.text("Edge not detected")
            res1="Edge not detected"

    with col2:
        UltraSonic=db.child('Motion').child('Distance').get()
        
        if UltraSonic.val()!=res:
           text_placeholder2.text(UltraSonic.val())
           res=UltraSonic.val()


    with col3:        
        orient=db.child('Motion').child('Orientation').get()
        if orient.val()!=check:
    
            if orient.val()==0:
                text_placeholder3.text("Stop")
            elif orient.val()==1:
                text_placeholder3.text("Forward")
            elif orient.val()==2:
                text_placeholder3.text("Backward")
            elif orient.val()==3:
                text_placeholder3.text("Left")
            elif orient.val()==4:
                text_placeholder3.text("Right")

            check=orient.val()


    with col4:
         obstacle=db.child('Motion').child('Obstacle').get()
         if obstacle.val()!=check2:
            if obstacle.val()==0:
                   text_placeholder4.text("No Obstacle")
            elif obstacle.val()==1:
                    text_placeholder4.text("Obstacle Detected")
            check2=obstacle.val()
    with col5:
        battery=db.child('Motion').child('Battery').get()
        battery1=battery.val()/11.1
        if battery1*100>70 and ans!="High":
            text_placeholder5.text("High")
            ans="High"
        elif battery1*100==50 and ans!="Medium":
            text_placeholder5.text("Medium")
            ans="Medium"
        elif battery1*100<=20 and ans!="Battery Low, Charge the battery":
            text_placeholder5.text("Battery Low, Charge the battery")
            ans="Battery Low, Charge the battery"

    # with  col6:
    #      velocity = [0, 0, 0]  # Initial velocity in x, y, z directions
    #      position = [0, 0, 0]  # Initial position in x, y, z directions
    #      last_time = time.time()
    #      accel_x=float(db.child('Motion').child('Accelerometer').child('0').get().val())
    #      accel_y=float(db.child('Motion').child('Accelerometer').child('1').get().val())
    #      accel_z=float(db.child('Motion').child('Accelerometer').child('2').get().val())
        
    #     # Calculate total acceleration and update velocity and position
    #      accel_total = math.sqrt(accel_x**2 + accel_y**2 + accel_z**2)
    #      current_time = time.time()
    #      delta_t = current_time - last_time
    #      velocity[0] += accel_x * delta_t
    #      velocity[1] += accel_y * delta_t
    #      velocity[2] += accel_z * delta_t
    #      position[0] += velocity[0] * delta_t
    #      position[1] += velocity[1] * delta_t
    #      position[2] += velocity[2] * delta_t
         
    #      last_time = current_time

    #      text_placeholder6.text(f"Current position: x={position[0]}, y={position[1]}, z={position[2]}")
