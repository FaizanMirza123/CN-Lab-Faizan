import socket
import sys

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    add = ('localhost', 10000)
    
    try:
        sock.connect(add)
        
        sock.sendall("Hello, This is Client".encode()) 

        server_message = ""
        while True:
            data = sock.recv(16) 
            if not data:
                break  
            server_message += data.decode()

        print("Server Response:", server_message)

    except Exception as e:
        print(e)

    finally:
        sock.close()


if __name__ == "__main__":
    main()
