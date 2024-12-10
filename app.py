import os
import subprocess
import sys
import time
from flask_app import start_flask_app  # Ensure this import is correct

def kill_process_using_port(port):
    try:
        import psutil  # Import psutil to check for processes
        for proc in psutil.process_iter(attrs=['pid', 'connections']):
            for conn in proc.info['connections']:
                if conn.laddr.port == port:
                    proc.terminate()  # Kill the process using the port
                    print(f"Terminated process using port {port}")
    except ImportError:
        print("psutil module is not installed.")
        sys.exit(1)

if __name__ == "__main__":
    port = 5000
    kill_process_using_port(port)
    start_flask_app()
