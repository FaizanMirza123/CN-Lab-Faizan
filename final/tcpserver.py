import socket
import threading

def main():
    server_address="127.0.0.1"
    server_port=2000
    
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.bind((server_address,server_port))
        sock.listen(1)
        print("Listening..")
    except Exception as e:
        print(e)
        return
    
    while True:
        client_socket,_=sock.accept()
        t=threading.Thread(target=testfunction,args=(client_socket,))
        t.start()

def testfunction(client_socket):
    try:
        client_message=client_socket.recv(2000).decode()
        print(f"Client's Message: {client_message}")
        
        client_socket.sendall(("Hello This is TCP server").encode())
        
        client_message=client_socket.recv(2000).decode()
        client_socket.sendall(("My second message").encode())
    except Exception as e:
        print(e)
    client_socket.close()
if __name__=="__main__":
    main()