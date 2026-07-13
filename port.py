import socket

def check_port(host, port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)  # Timeout of 2 seconds

        # Check if the port is open
        result = s.connect_ex((host, port))

        if result == 0:
            print(f"Port {port} is OPEN on {host}.")
        else:
            print(f"Port {port} is CLOSED on {host}.")

        s.close()

    except socket.gaierror:
        print("Error: Invalid hostname or IP address.")
    except ValueError:
        print("Error: Please enter a valid port number.")
    except Exception as e:
        print("Error:", e)


# Main Program
host = input("Enter Hostname or IP Address: ")
port = int(input("Enter Port Number: "))

check_port(host, port)