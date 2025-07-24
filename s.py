import socket
import threading

def handle_client(client_socket):
    while(True):
        try:
            message=client_socket.recv(1024).decode()
            if not message:
                print("Client  disconnected")
                break
            print("Client says:",message)
            reply=input("Server says: ")
            client_socket.sendall(message.encode())
        except Exception as e:
            print("Error",e)
            break
    client_socket.close()

def main():
    host="0.0.0.0"
    port=12345
    clients = []
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((host,port))
    server.listen(5)
    print(f"Server listening on {host}:{port}")
    while True:
        client,addr=server.accept()
        print("connected with",addr)
        client_handler=threading.Thread(target=handle_client,args=(client))
        client_handler.start()

if __name__ == "__main__":
    main()