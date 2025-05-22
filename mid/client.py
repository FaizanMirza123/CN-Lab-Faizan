import socket

def main():

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('127.0.0.1', 2000)

    try:
        while True:
            client_message = input("Connect with resturant")

            message=client_message[:7]
            if(message!="Connect"):
                print("Wrong Syntax")
            else:
                break
            
        sock.sendto(client_message.encode(), server_address)

     
        server_message, _ = sock.recvfrom(2000)
        print(f"Resturant Respond: {server_message.decode()}")
        
        order=input("Order, Cancel, Exit")
        sock.sendto(order.encode(), server_address)
        
        server_message, _ = sock.recvfrom(2000)
        print(f"Resturant Respond: {server_message.decode()}")
        
        message= input(server_message.decode())
        
        sock.sendto(message.encode(), server_address)
        
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        sock.close()

if __name__ == "__main__":
    main()