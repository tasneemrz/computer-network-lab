import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)
print(f"server listening on {HOST}, {PORT}")

while True:
    conn_socket, addr = server.accept()
    print(f"[CONNECTED TO] : {addr}")

    while True:
        msgFromClient = conn_socket.recv(1024).decode('utf-8')

        if(msgFromClient):
            print(f"\nClient : {msgFromClient}")
            msgToSend = input("-> ")
            conn_socket.send(msgToSend.encode('utf-8'))
            
        else:
            print("[CLIENT HAS DISCONNECTED!]")
            conn_socket.close()
