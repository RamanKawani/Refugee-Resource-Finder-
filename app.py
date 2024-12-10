import os
import signal
import subprocess
import sys
import time

def kill_process_using_port(port):
    try:
        # Check and kill the process using the port
        pid = subprocess.check_output(["fuser", f"{port}/tcp", "-k"])
        print(f"Process using port {port} has been killed.")
    except subprocess.CalledProcessError:
        print(f"No process found using port {port}.")

def restart_flask_app():
    print("Restarting Flask app...")
    os.execv(sys.executable, ['python'] + sys.argv)

if __name__ == "__main__":
    port = 5000  # Flask app port

    # Check if the port is being used
    try:
        print("Checking if port 5000 is in use...")
        kill_process_using_port(port)

        # Import and run the Flask app from flask_app.py
        print("Starting Flask app...")
        from flask_app import start_flask_app
        start_flask_app()

    except OSError as e:
        if e.errno == 98:  # Address already in use
            print(f"Port {port} is already in use, attempting to kill the process.")
            kill_process_using_port(port)
            time.sleep(1)  # Give time for the process to terminate
            restart_flask_app()
        else:
            raise
