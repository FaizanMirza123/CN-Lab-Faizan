import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Connected to {client_address}")
    try:
        message = client_socket.recv(1024).decode()
        print(f"Received: {message}")
        client_socket.sendall(message.encode())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

def main():
    host = '127.0.0.1'
    port = 2000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Server listening...")

    while True:
        client_socket, client_address = server_socket.accept()
        t = threading.Thread(target=handle_client, args=(client_socket, client_address))
        t.start()

if __name__ == "__main__":
    main()
