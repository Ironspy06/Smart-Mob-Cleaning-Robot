import cv2 as cv
import numpy as np
import pyrebase
import random
import streamlit as st
import time
import matplotlib.pyplot as plt
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

x = 500
y = 500
points = [(0, 0), (0, 0)]

points1 = [(0, 0), (0, 0)]

# a=0
movement = [0]  # 0,3,1  0,1
flag = -1
flag1 = -1
flag2 = -1
flag3 = -1
flag4 = -1
flag5 = -1
x1 = 0
y1 = 0
valid = True
area=10

def Movement():
    global x, y, x1, y1, flag1, flag, flag2, flag3, flag4, flag5
    orient1 = db.child('Motion').child('Orientation').get()
    # UltraSonic = db.child('Motion').child('US').get()
    #valid=db.child('Motion').child('Valid').get()
    if orient1.val() == 1:  # forward  and valid.val()==1

        if orient1.val() != flag1:
            movement.append(orient1.val())
            flag1 = orient1.val()

        if movement[-2] == 3:
            x1 = x - 10
            y1 = y
            movement.pop(1)
            flag = -1
        if movement[-2] == 4:
            x1 = x + 10
            y1 = y
            movement.pop(1)
            flag3 = -1
        if movement[-2] == 2:
            x1 = x
            y1 = y + 10
            movement.pop(1)
            flag5 = -1
        y -= 10
    if orient1.val() == 2:  # backward
        if orient1.val() != flag5:
            movement.append(orient1.val())
            flag5 = orient1.val()
            if movement[-2] == 3:
                x1 = x - 10
                y1 = y
                movement.pop(1)
                flag = -1
            if movement[-2] == 4:
                x1 = x + 10
                y1 = y
                movement.pop(1)
                flag3 = -1
            if movement[-2] == 1:
                x1 = x
                y1 = y - 10
                movement.pop(1)
                flag1 = -1
        y += 10
    if orient1.val() == 3:  # left

        if orient1.val() != flag:
            movement.append(orient1.val())
            flag = orient1.val()
        print(movement)
        if movement[-2] == 1:
            x1 = x
            y1 = y - 10
            movement.pop(1)
            flag1 = -1
        if movement[-2] == 2:
            x1 = x
            y1 = y + 10
            movement.pop(1)
            flag5 = -1
        if movement[-2] == 4:
            x1 = x + 10
            y1 = y
            movement.pop(1)
            flag3 = -1
        x -= 10

    if orient1.val() == 4:  # right
        if orient1.val() != flag3:
            movement.append(orient1.val())
            flag3 = orient1.val()
        print(movement)
        if movement[-2] == 1:
            x1 = x
            y1 = y - 10
            movement.pop(1)
            flag1 = -1
        if movement[-2] == 2:
            x1 = x
            y1 = y + 10
            movement.pop(1)
            flag5 = -1
        if movement[-2] == 3:
            x1 = x - 10
            y1 = y
            movement.pop(1)
            flag = -1

        x += 10
    else:
        x += 0
        y += 0

    return [x, y, x1, y1]


def valid(points):
    for i in range(0, len(points) - 1):
        if points[-1][0] == points[i][0] and points[-1][1] == points[i][1]:
            data = {"Valid": 0}
            db.child("Motion").update(data)
            break
        else:
            data = {"Valid": 1}
            db.child("Motion").update(data)


def automaticMovement():
    global x, y
    x += random.randint(0, 1)
    y += random.randint(-1, 1)

    return [x, y]


def drawObj(img2, points2):
    # if x!=0 and y!=0:
    for point in points2:
        cv.circle(img2, point, 8, (255, 0, 0), cv.FILLED)


def text(img2, points2):
    for i in range(2, len(points2)):
        cv.putText(img2, f'({(points2[i][0] - 500) / 100},{-(points2[i][1] - 500) / 100})m',
                   (points2[i][0] + 10, points2[i][1] + 30), cv.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 1)


def drawPoints(img1, Points1):
    cell_count=0
    for point in Points1:
        cv.circle(img1, point, 5, (0, 0, 255), cv.FILLED)
        cell_count=cell_count+1
    cv.circle(img1, Points1[-1], 8, (0, 255, 0), cv.FILLED)

    cv.putText(img1, f'({(Points1[-1][0] - 500) / 100},{-(Points1[-1][1] - 500) / 100})m',
               (Points1[-1][0] + 10, Points1[-1][1] + 30), cv.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 1)
st.header("Environment Mapping")
size = (80, 80)

# Create a Streamlit placeholder for the image
image_placeholder = st.empty()
# def forward():
#    data={"Orientation":1}
#    db.child("Motion").update(data)
# def Backward():
#    data={"Orientation":2}
#    db.child("Motion").update(data)
# def left():
#    data={"Orientation":3}
#    db.child("Motion").update(data)

# def right():
#    data={"Orientation":4}
#    db.child("Motion").update(data)
# def stop():
#    data={"Orientation":0}
#    db.child("Motion").update(data)
# f=st.button(label='Forward', on_click=forward)
# b=st.button(label='Backward', on_click=Backward)
# l=st.button(label='Left', on_click=left)
# r1=st.button(label='Right', on_click=right)
# s1=st.button(label='Stop', on_click=stop)
while True:
    count=0
    vals2 = Movement()  # automatic motion mapping code
    # print(vals2[0],vals2[1])
    img = np.zeros((1000, 1000, 3), np.uint8)
    if points[-1][0] != vals2[0] or points[-1][1] != vals2[1]:
        points.append((vals2[0], vals2[1]))
    # img = np.zeros((1000, 1000, 3), np.uint8)
    # if(points[-1][0]!=vals[0] or points[-1][1]!=vals[1]):
    #     points.append((vals[0], vals[1]))
    if points1[-1][0] != vals2[2] or points1[-1][1] != vals2[3]:
        points1.append((vals2[2], vals2[3]))

    #valid(points)
    drawPoints(img, points)
    count+=1
    drawObj(img, points1)
    text(img, points1)

    # print(points)
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    cv.imshow("Output", img_rgb)
    image_placeholder.image(img_rgb)
    cv.waitKey(1)
