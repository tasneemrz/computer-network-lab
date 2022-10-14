import socket

HOST = '192.168.1.9'
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    msg = input("-> ").encode('utf-8')
    client.send(msg)
    msg_from_server = client.recv(1024).decode('utf-8')
    if(msg_from_server):
        print(f"server: {msg_from_server}")
    else:
        print("[SERVER DISCONNECTED]")
        client.close()
