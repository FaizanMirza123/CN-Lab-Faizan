import socket

def main():
 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    
    server_address = ('127.0.0.1', 2000)
    sock.bind(server_address)

    print("Resturant Started")

    while True:
        try:
           
            client_message, client_address = sock.recvfrom(2000)
            order = client_message.decode().strip()

            print(f"Customer Message: {order}")
            
            name=order[7:]
                
            sock.sendto(("Welcome:"+name).encode(), client_address)
            
            client_message, client_address = sock.recvfrom(2000)
            
            order = client_message.decode().strip()
        
            if(order=="Exit"):
                sock.sendto(("Goodbye:"+name).encode(), client_address)
                break
            elif(order=="Order"):
                sock.sendto(("Tell your order:").encode(), client_address)
                client_message, client_address = sock.recvfrom(2000)
                f=open("C:/Users/faiza/OneDrive/Desktop/mid/menu.txt")
                message=f.read()
               
                if "pizza" in  client_message.decode():
                    sock.sendto("pizza available".encode(),client_address)
                if "burger" in  client_message.decode():
                    print("pizza available")
                if "pasta" in  client_message.decode():
                    print("pizza unavailable")
                    
                
            elif(order=="Cancel"):
                print("Canceled")
        except Exception as e:
            print(f"An error occurred: {e}")
            break

    sock.close()

if __name__ == "__main__":
    main()
