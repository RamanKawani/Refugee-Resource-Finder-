import os
import signal
import subprocess
import sys
import time

def kill_process_using_port(port):
    try:
        # Try to find processes using 'lsof' (Linux/macOS) or 'netstat' (Windows)
        print(f"Checking if port {port} is in use...")
        
        # Using lsof command to find processes (works on Linux/macOS)
        result = subprocess.run(['lsof', '-t', f'-i:{port}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # If 'lsof' fails, try 'netstat' (works on Windows)
        if result.returncode != 0:
            print(f"'lsof' failed. Trying 'netstat' for port {port}...")
            result = subprocess.run(['netstat', '-ano'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode == 0:
            process_ids = result.stdout.decode().strip().splitlines()
            for pid in process_ids:
                pid = pid.strip()
                if pid:
                    print(f"Killing process with PID {pid} on port {port}")
                    # Kill the process using the pid
                    subprocess.run(['kill', '-9', pid], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    print(f"Process {pid} terminated.")
                else:
                    print(f"No process found using port {port}.")
        else:
            print(f"Could not determine process using port {port}.")
    
    except Exception as e:
        print(f"Error occurred while trying to kill the process: {str(e)}")

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
