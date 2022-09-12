import socket
import json
import threading

PORT = 9999
SERVER = socket.gethostbyname(socket.gethostname())  
ADDR = (SERVER, PORT)
HEADER = 1024
DISCONNECTION_MSG = ';;'
FORMAT = 'utf-8' 

client = socket.socket()  
client.connect(ADDR)   

def prGreen(skk): 
    print("\033[92m{}\033[00m" .format(skk))  

# a utility to send message with ability to calculate the header buffer automatically making it optimised
def send(message):
    msg = message.encode(FORMAT)
    msg_length = len(msg)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(msg)

def handle_msg():
    msg = client.recv(1024).decode()
    prGreen(msg)
    
name = input("Enter your name :")
client.send(bytes(name, FORMAT))

while True:
    thread = threading.Thread(target = handle_msg)
    thread.start()
    msg = input("-> ")

    if msg == DISCONNECTION_MSG:
        print("Closing your connection !!!")
        send(msg)
        break
    
    send(msg)