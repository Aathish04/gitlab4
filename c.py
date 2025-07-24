import socket
import threading

def main():
    host="10.16.65.45"
    port=12345

    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host,port))

    while True:
        try:
            message=input("Enter the message:")
            client.sendall(message.encode())
            reply=client.recv(1024).decode()
            print("Server says:",reply)
        except Exception as e:
            print("Error",e)
            break
    client.close()

if __name__ == "__main__":
    main()