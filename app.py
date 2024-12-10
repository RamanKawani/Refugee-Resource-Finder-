import streamlit as st
from waitress import serve
from flask_app import create_app

# Create the Flask app
app = create_app()

# Streamlit content
st.title("Refugee Resource Finder")

# Button to start the Flask app in the background
if st.button("Start Flask App"):
    # Serve Flask app using Waitress
    serve(app, host="0.0.0.0", port=8080)
    st.success("Flask app is running on port 8080!")
