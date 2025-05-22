import socket

def main():
 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    
    server_address = ('127.0.0.1', 2000)
    sock.bind(server_address)
    
    lst = [] 
    
    print("Socket created and bound")
    print("Listening for messages...\n")

    while True:
        try:
           
            client_message, client_address = sock.recvfrom(2000)
            roll = client_message.decode().strip()

            print(f"Received message from IP: {client_address[0]} and Port No: {client_address[1]}")
            print(f"Client Message: {roll}")

            user_id = roll[:-3]  
            action = roll[-2:]  

            if action == "CI":  
                print("Members in Database:") 
                for x in lst:
                    print(x)
                if user_id in lst:
                    sock.sendto("You are already checked in.".encode(), client_address)
                else:
                    lst.append(user_id)  
                    sock.sendto(("Welcome Student " + user_id).encode(), client_address)

            elif action == "CO":
                print("Members in Database:") 
                for x in lst:
                    print(x)
                if user_id in lst:
                    lst.remove(user_id)  
                    sock.sendto(("Goodbye Student " + user_id + ". Have a Nice Day!").encode(), client_address)
                else:
                    sock.sendto("You didn’t check in today. Contact System Administrator.".encode(), client_address)

            else:
                sock.sendto("Invalid request".encode(), client_address)

        except Exception as e:
            print(f"An error occurred: {e}")
            break

    sock.close()

if __name__ == "__main__":
    main()
