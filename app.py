import os
import signal
import subprocess
import sys
import time
import psutil  # Import psutil to check for processes

def kill_process_using_port(port):
    try:
        # Check all running processes to find one that is using the port
        for proc in psutil.process_iter(['pid', 'name', 'connections']):
            for conn in proc.info['connections']:
                if conn.laddr.port == port:
                    print(f"Killing process {proc.info['name']} with PID {proc.info['pid']} on port {port}")
                    proc.terminate()  # Terminate the process
                    proc.wait()  # Wait for process termination
                    return
        print(f"No process found using port {port}.")
    except psutil.NoSuchProcess:
        print(f"Error: Process not found while trying to kill on port {port}.")
    except psutil.AccessDenied:
        print(f"Error: Access denied while trying to terminate the process.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

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
