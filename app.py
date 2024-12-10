import psutil
import os
import signal
import logging

# Set up logging to output useful information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def kill_process_using_port(port=5000):
    try:
        logging.info(f"Checking for processes using port {port}...")

        # Iterate over all processes and their open connections
        for proc in psutil.process_iter(attrs=['pid', 'name', 'connections']):
            try:
                for conn in proc.info['connections']:
                    if conn.laddr.port == port:  # Check if this process is using the specified port
                        logging.info(f"Process {proc.info['name']} (PID {proc.info['pid']}) is using port {port}. Terminating...")
                        proc.terminate()  # Terminate the process using the port
                        proc.wait(timeout=3)  # Ensure the process is terminated
                        logging.info(f"Process {proc.info['name']} (PID {proc.info['pid']}) has been terminated.")
                        return  # Exit once the process has been killed
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue  # Handle processes that have been closed or are inaccessible

        logging.info(f"No process was found using port {port}.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def start_streamlit_app():
    try:
        logging.info("Starting Streamlit app...")
        os.system("streamlit run app.py")  # Command to run the Streamlit app
    except Exception as e:
        logging.error(f"Failed to start Streamlit app: {e}")

if __name__ == "__main__":
    port = 5000  # You can change this port number if needed
    kill_process_using_port(port)
    start_streamlit_app()
