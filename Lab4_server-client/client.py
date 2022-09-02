import socket

HOST = '192.168.1.9'
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    msgToSend = input("-> ")
    client.send(msgToSend.encode('utf-8'))
    msgFromServer = client.recv(1024).decode('utf-8')

    if(msgFromServer):
        print(f"Server : {msgFromServer}")
