
import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    add = ('localhost', 10000)
    sock.bind(add)
    sock.listen()
    
    while True:
        connection, client_address = sock.accept()
        try:
            data = connection.recv(1024)  
            if data:
                received_text = data.decode()
                reversed_text = received_text[::-1]
                connection.sendall(reversed_text.encode())  
                print(f"Received: {received_text}")
        except Exception as e:
            print(e)
        finally:
            connection.shutdown(socket.SHUT_WR)
            connection.close()

if __name__ == "__main__":
    main()