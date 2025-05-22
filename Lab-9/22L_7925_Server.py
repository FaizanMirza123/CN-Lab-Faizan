import socket
import threading
import re

        
def handleVotes(client_socket,candidates,polls,voters,Unique):
    try:
        print("New Client Connected")
        client_message=client_socket.recv(1024).decode()
        print(client_message)
        
        if client_message in voters and client_message not in Unique:
             
             client_socket.sendall(("CNIC/Name Matched ").encode())
             client_name=client_message
             message = "\n".join(candidates)
             client_socket.sendall((message).encode())
             client_message=client_socket.recv(1024).decode()
             print(client_message)
             if client_message in polls:
                 client_socket.sendall(("Candidate is Voted, Voting Ends").encode())
                 Unique.append(client_name)
                 with open("output","w") as f:
                     f.write("Voter: "+client_name +" Symbol Voted:"+ client_message)
             else:
                 client_socket.sendall(("Candidate doesn't exist, Voting Ends").encode())
        elif client_message in Unique:
             client_socket.sendall(("Corruption??\n Go away you already voted").encode())
             client_socket.sendall(("Voting Ends").encode())
        else:
            client_socket.sendall(("CNIC/Name doesn't exist").encode())
            client_socket.sendall(("Voting Ends").encode())
             
       
    except Exception as e:
        print(e)
    client_socket.close()
def main():
    
        f=open("Candidates_List")
        candidates=f.read()
        candidates=candidates.split('\n')
    
        polls=[poll.strip().split()[-1] for poll in candidates if poll.strip()]
        
        f=open("Voters_List")
        voters=f.read()
        voters=voters.split('\n')
        
        Unique=[]
        host = '127.0.0.1'  
        port = 2000
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Socket created")
        except socket.error as err: 
            print(f"Could not create socket. Error: {err}")
            return

        try:
            server_socket.bind((host, port))
            print("Bind done")
        except socket.error as err:
            print(f"Bind failed. Error: {err}")
            return

        try:
            
            server_socket.listen(1)
            print("Listening for incoming connections...")
        except socket.error as err:
            print(f"Listen failed. Error: {err}")
            return
        while True:
            client_socket,_=server_socket.accept()
            t=threading.Thread(target=handleVotes,args=(client_socket,candidates,polls,voters,Unique))
            t.start()
        

if __name__ == "__main__":
    main()