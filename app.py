mport os
import signal
import subprocess
from flask import Flask
from waitress import serve

def kill_port_5000():
    """Find and kill the process using port 5000."""
    try:
        # Find the process ID using the port 5000
        result = subprocess.run(['lsof', '-t', '-i', ':5000'], stdout=subprocess.PIPE)
        pid = result.stdout.decode().strip()
        if pid:
            print(f"Terminating process using port 5000, PID: {pid}")
            os.kill(int(pid), signal.SIGKILL)
        else:
            print("No process found using port 5000.")
    except Exception as e:
        print(f"Error while killing the process: {e}")

# Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == "__main__":
    # Kill any process occupying port 5000
    kill_port_5000()

    # Start the Flask app using Waitress
    print("Starting Flask app...")
    serve(app, host='0.0.0.0', port=5000)
