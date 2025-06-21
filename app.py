from demo import area_of_circle
import streamlit as st

st.title("Hello, Streamlit!")
st.write("Welcome to your first Streamlit app.")

name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")

radius = st.number_input("Enter the radius of a circle:", min_value=0.0, step=0.1)
if st.button("Calculate Area"):
    a = area_of_circle(radius)
    st.write(f"The area of the circle is {a}")