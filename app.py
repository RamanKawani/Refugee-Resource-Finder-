import os
import signal
import subprocess
import sys
import time
import psutil

def kill_process_using_port(port):
    try:
        # Try to find processes using psutil (cross-platform)
        print(f"Checking if port {port} is in use...")
        
        # Loop through all processes and check for port usage
        for proc in psutil.process_iter(['pid', 'connections']):
            for conn in proc.info['connections']:
                if conn.status == 'LISTEN' and conn.laddr.port == port:
                    print(f"Process {proc.info['pid']} is using port {port}. Terminating...")
                    proc.terminate()  # Try terminating the process
                    proc.wait()  # Wait for termination
                    print(f"Process {proc.info['pid']} terminated.")
                    return
        
        print(f"No process found using port {port}.")

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
