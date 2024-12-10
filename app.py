import psutil
import streamlit as st

# Function to kill the process using the specified port
def kill_process_using_port(port):
    try:
        for proc in psutil.process_iter(['pid', 'connections']):
            try:
                # Check for connections that are using the specified port
                for conn in proc.connections(kind='inet'):
                    if conn.laddr.port == port:
                        proc.terminate()  # Terminate the process using the port
                        st.write(f"Terminated process {proc.info['pid']} using port {port}")
                        return
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
    except Exception as e:
        st.write(f"Error: {e}")

# Streamlit app logic
def main():
    # Show a title
    st.title('Streamlit Port Killer')

    # Port to check and kill processes
    port = 5000

    # Try to kill the process using the port
    kill_process_using_port(port)

    # Display a message that the app is running
    st.write(f"Streamlit app is running on port {port}")

# Run the Streamlit app
if __name__ == "__main__":
    main()
