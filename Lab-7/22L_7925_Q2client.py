import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    add = ('localhost', 10000)
    
    try:
        sock.connect(add)
        text_to_send = input("Enter text to reverse: ")
        sock.sendall(text_to_send.encode()) 

        reversed_text = ""
        while True:
            data = sock.recv(16) 
            if not data:
                break  
            reversed_text += data.decode()

        print("Reversed Text from Server:", reversed_text)

    except Exception as e:
        print(e)

    finally:
        sock.close()

if __name__ == "__main__":
    main()
