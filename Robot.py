import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Robot Website"
)
st.title("Smart Mop-Rob (Autonomous Robotic Vacuum)​")
st.subheader("INTRODUCTION")
st.write("The robotic cleaners have taken major attention in robotics research due to their effectiveness in assisting humans in floor cleaning applications at homes, hotels, restaurants, offices, hospitals, warehouses, and educational institutions, etc. It is an electromechanical machine and used for various purposes in domestic applications. Although devices such as washing machines and dishwashers have served this purpose, it still requires some degree of human input effort. In developing a floor cleaning robot, there are several challenges that one has to come in front, i.e. the method of cleaning, path planning, covering the whole floor surface, cleaning it completely, maintenance so on and so forth. It becomes even more complicated when safety, economy, energy consumption are considered to be at the optimum level. Initially, the main focus was on having a household cleaning device robot.")
st.subheader("AIM")
st.write("The main aim of this project is to design and develop a fully autonomous robotic vacuum with dirt detection capabilities which is cost effective and avoids drawbacks contained in its current literature, with novel concepts.​")
st.subheader("FEATURES")
image = Image.open('img1.png')

st.image(image)

st.subheader("RESULT")
image1 = Image.open('img2.png')

st.image(image1)
st.write("")
st.write("")
st.write("DONE BY:-")
st.write("Pratik S Rao, M BalaSubramanium, Mohammed Shakeel, Kunal B Yellurkar :)")
#st.sidebar.camera_input("Camera")
