import socket
import subprocess
from datetime import datetime

def port_scanning(ip, startPort, endPort):
    for port in range(startPort, endPort + 1):
        try:

            # "socket.AF_INET" signifies that we are using IPv4 at the network layer and "socket.SOCK_STREAM" signifies that we are using TCP at the transport layer
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            error_code = connection.connect_ex((ip, port))
            
            # On succesfully connecting to a port the error code returned is 0 meaning that the port is open
            if error_code == 0:
                print(f"Port {port}: Open")
            connection.close()
            
        except Exception:
            print("Unexpected Error Occurred.")


def main():

    # Clears your Shell window
    subprocess.call('cls', shell = True) 

    # Time before the program gives up on recieving a connection response from the port and moves on to scan the next one (in seconds)
    socket.setdefaulttimeout(0.1)

    start_port = int(input("Enter the Start Port: "))
    end_port = int(input("Enter the End Port: "))
    ip_address_or_url = input("Enter the IP Address or the URL of the webpage you want to Ping: ")

    print("Port Scanning Started")

    # sTime stores the time at which the port scanning started
    sTime = datetime.now()
    port_scanning(ip_address_or_url, start_port, end_port)
    # eTime stores the time at which the port scanning concluded
    eTime = datetime.now()
    timeDef = eTime - sTime

    print(f"Port Scanning Completed. Time Taken: {timeDef}")

main()