import streamlit as st
from waitress import serve
from flask_app import create_app

# Create the Flask app
app = create_app()

# This function will run the Flask app using Waitress server
def run_flask_app():
    serve(app, host='0.0.0.0', port=5000)

# You can add your Streamlit UI components here if needed
st.title("Refugee Resource Finder")
st.write("Welcome to the Refugee Resource Finder platform!")

# Streamlit command to run the Flask app in the background
if __name__ == '__main__':
    run_flask_app()
