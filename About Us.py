import streamlit as st
from PIL import Image
st.header("MEET OUR TEAM")
st.write("We are the students of Jss Academy of Technical Education Bangalore currently pursing our Bachelors in Engineering (2019-2023).")
col1, col2 = st.columns(2)
with col1:

    image = Image.open('Bala1.jpeg')
    st.image(image,width=150)
    st.write("M Balasubramanium(CSE)")
   

    image = Image.open('Pratik.jpeg')
    st.image(image,width=150)
    st.write("Pratik S Rao(CSE)")

with col2:

    image = Image.open('Shankar.jpeg')
    st.image(image,width=150)
    st.write("Shankar Singh(ECE)")
    image = Image.open('Sumanth.JPG')
    st.image(image,width=150)
    st.write("Sumanth Rao(ECE)")
