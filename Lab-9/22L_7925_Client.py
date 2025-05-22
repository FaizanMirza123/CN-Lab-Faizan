import socket

def main():
    # Define server details
    server_ip = '127.0.0.1'
    server_port = 2000
    buffer_size = 2000

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket created")
    except socket.error as err:
        print(f"Could not create socket. Error: {err}")
        return

  
    try:
        client_socket.connect((server_ip, server_port))
        print("Connected to server")
    except socket.error as err:
        print(f"Connection failed. Error: {err}")
        return

    client_message = input("Enter in Name/CNIC ")

  
    try:
        client_socket.sendall(client_message.encode())
    except socket.error as err:
        print(f"Send failed. Error: {err}")
        client_socket.close()
        return
   
    try:
        server_message = client_socket.recv(buffer_size).decode()
        print(f"Server Message: {server_message}")
    except socket.error as err:
        print(f"Receive failed. Error: {err}")
        
    try:
        server_message = client_socket.recv(buffer_size).decode()
        print(f"Server Message1: {server_message}")
        if(server_message == "Voting Ends"):
            return
    except socket.error as err:
        print(f"Receive failed. Error: {err}")

   
    client_message = input("Enter Candidate Symbol: ")

    try:
        client_socket.sendall(client_message.encode())
    except socket.error as err:
        print(f"Send failed. Error: {err}")
        client_socket.close()
        return

   
    try:
        server_message = client_socket.recv(buffer_size).decode()
        print(f"Server Message: {server_message}")
    except socket.error as err:
        print(f"Receive failed. Error: {err}")

    
    client_socket.close()

if __name__ == "__main__":
    main()