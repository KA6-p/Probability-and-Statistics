import streamlit as st

# Title of the app
st.title("My First Streamlit App")

# Subtitle
st.subheader("Welcome to my Streamlit App")

# A simple text
st.write("This is my first web app using Streamlit!")

# Add a button
if st.button("Click Me!"):
    st.write("You clicked the button! 🎉")
st.text_input("Enter your name:")
st.slider("Select a number", 0, 100)


