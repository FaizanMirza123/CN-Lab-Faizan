import socket

def main():
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    server_address=('127.0.0.1',2000)
    sock.bind(server_address)
    
    lst=[]
    
    print("listening for messages")
    
    while True:
        try:
            client_message,client_address=sock.recvfrom(2000);
            
            message=client_message.decode();
            
            print(f"Connection established with {client_address[0]}")
            
            sock.sendto(("I am good man ").encode(),client_address)
        except Exception as e:
            print("error")
            break
    sock.close()
if __name__ =="__main__":
    main()
        
        