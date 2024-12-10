import psutil
from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Function to kill the process using the specified port
def kill_process_using_port(port):
    try:
        for proc in psutil.process_iter(['pid', 'connections']):
            try:
                # Check for connections that are using the specified port
                for conn in proc.connections(kind='inet'):
                    if conn.laddr.port == port:
                        proc.terminate()  # Terminate the process using the port
                        print(f"Terminated process {proc.info['pid']} using port {port}")
                        return
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
    except Exception as e:
        print(f"Error: {e}")

# Define a simple route to check the app is running
@app.route('/')
def home():
    return "Flask app is running!"

# Main logic to run the application
if __name__ == "__main__":
    port = 5000  # The port to check and use for the Flask app
    kill_process_using_port(port)  # Try to kill the process using the port
    app.run(port=port)  # Start the Flask app on the specified port
