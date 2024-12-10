import streamlit as st
from waitress import serve
from your_flask_app import create_app
# Create the Flask app
app = create_app()

# Streamlit UI
st.title("My Refugee Resource Finder")
st.write("Welcome to the app!")

# If you need to run the Flask server with waitress in the background
if __name__ == "__main__":
    # Run Flask app with waitress in the background
    from threading import Thread

    def run_flask():
        serve(app, host='0.0.0.0', port=5000)

    # Run Flask in a separate thread
    thread = Thread(target=run_flask)
    thread.daemon = True
    thread.start()

    # Streamlit logic
    st.write("Streamlit is ready!")

