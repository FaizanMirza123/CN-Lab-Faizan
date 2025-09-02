import socket

def main():
    
    server_ip="127.0.0.1"
    server_port=2000
    buffer_size=2000
    
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    try:
        sock.connect((server_ip,server_port))
        print("Connection Established")
    except Exception as e:
        print("err")
        return
    
    client_message=input("Your message")
    
    try:
        sock.sendall(client_message.encode())
        server_message=sock.recv(buffer_size).decode()
        print(f"Server's Response: {server_message}")
        
        client_message=input("Second Message: ")
        sock.sendall(client_message.encode())
        
        server_message=sock.recv(buffer_size).decode()
        print(f"Server's Response: {server_message}")
    except Exception as e:
        print("error at messages")
    sock.close()
    
if __name__=="__main__":
    main()
    
    