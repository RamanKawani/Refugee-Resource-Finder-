import os
import sys
import time
import psutil

def kill_process_using_port(port):
    try:
        print(f"Checking if port {port} is in use...")
        
        # Check processes using the port
        for proc in psutil.process_iter(['pid', 'connections']):
            for conn in proc.info['connections']:
                if conn.status == 'LISTEN' and conn.laddr.port == port:
                    print(f"Found process {proc.info['pid']} using port {port}. Terminating...")
                    proc.terminate()  # Terminate the process
                    proc.wait()  # Wait until the process is killed
                    print(f"Process {proc.info['pid']} terminated.")
                    return
        
        print(f"No process found using port {port}.")
    except Exception as e:
        print(f"Error checking port: {e}")

def restart_flask_app():
    print("Restarting Flask app...")
    os.execv(sys.executable, ['python'] + sys.argv)

if __name__ == "__main__":
    port = 5000

    try:
        # Check if port is in use
        kill_process_using_port(port)

        # Import and run Flask app
        print("Starting Flask app...")
        from flask_app import start_flask_app
        start_flask_app()

    except OSError as e:
        if e.errno == 98:  # Port in use error
            print(f"Port {port} is already in use. Attempting to kill the process.")
            kill_process_using_port(port)
            time.sleep(1)  # Give time for process to terminate
            restart_flask_app()
        else:
            raise
