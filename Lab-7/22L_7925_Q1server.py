import socket
import sys

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    add = ('localhost', 10000)
    sock.bind(add)
    sock.listen()
    i = 0

    while True:
        connection, client_address = sock.accept()

        try:
            data = connection.recv(1024)  
            if data:
                i += 1
                response = f"Hello, I am Server. Your received code is {i}"
                connection.sendall(response.encode())  
                recieved=data.decode()
                recieved+=f". My code is {i}"
                print(recieved)
        except Exception as e:
            print(e)
        finally:
            connection.shutdown(socket.SHUT_WR)
            connection.close()
            

if __name__ == "__main__":
    main()
