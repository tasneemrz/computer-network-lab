import socket
import threading
import os
import json
import time

PORT = 9999
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)
HEADER = 1024
DISCONNECTION_MSG = ';;'
FORMAT = 'utf-8' 
CONNECTIONS = []
ConnName = {}

server = socket.socket()
server.bind(ADDR)   

def handle_client(conn, addr):
    print(f"[CONNECTED TO] : {addr}")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)

        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECTION_MSG:
                print(f"[ {addr} HAS DISCONNECTED! ]")
                connected = False

            name = ConnName[conn]
            msg = name + " : " + msg

            for cli in CONNECTIONS:
                if cli!=conn:
                    cli.send(bytes(msg,FORMAT))

    conn.close()   

def start():
    server.listen()
    print(f"server listening on {HOST}, {PORT}")
    
    while True:
        conn, addr = server.accept()
        CONNECTIONS.append(conn)
        name  = conn.recv(1024).decode(FORMAT)
        ConnName[conn] = name
        thread = threading.Thread(target=handle_client, args=(conn, addr))  # used threading to make handling of clients async
        thread.start()  #starting a new thread every time new clients join

start()