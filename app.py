import psutil
import os
import signal
import logging

# Setup logging for better debugging
logging.basicConfig(level=logging.INFO)

# Function to check and kill the process using a specific port
def kill_process_using_port(port):
    logging.info(f"Checking for processes using port {port}...")

    # Iterate over all running processes
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        try:
            # Check if the process has a connection to the specified port
            for conn in proc.connections(kind='inet'):
                if conn.laddr.port == port:
                    logging.info(f"Found process {proc.info['name']} (PID: {proc.info['pid']}) using port {port}. Terminating...")
                    proc.terminate()
                    return
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    logging.info(f"No process found using port {port}.")

# Function to start Flask app (or any server you're using)
def start_flask_app():
    logging.info("Starting Streamlit app...")
    os.system("streamlit run app.py")

if __name__ == "__main__":
    port = 5000
    kill_process_using_port(port)
    start_flask_app()
