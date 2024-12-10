import psutil

def kill_process_using_port(port):
    try:
        # Iterate over all processes
        for proc in psutil.process_iter(attrs=['pid']):
            # Check if the process has any network connections
            for conn in proc.connections(kind='inet'):
                # If the connection is using the specified port
                if conn.laddr.port == port:
                    # Terminate the process using the port
                    proc.terminate()
                    print(f"Terminated process {proc.info['pid']} using port {port}")
                    return  # Exit once the process is terminated
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    port = 5000  # Change to your desired port number
    kill_process_using_port(port)
