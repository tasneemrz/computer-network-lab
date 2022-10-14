import socket
import string
import re

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)
print(f"server is listening on {HOST}")

def find_special_char(msg):
   ic = set(string.punctuation)
   if any(char in ic for char in msg):
        return True
   else:
        return False

def find_digit(msg):
   ic = set(string.digits)
   if any(digit in ic for digit in msg):
        return True
   else:
        return False

def find_char(msg):
    return bool(re.match('[a-zA-Z]',msg))

while True:
    conn_socket, addr = server.accept()
    print(f"Connected to {addr}")

    while True:
        message = conn_socket.recv(1024).decode('utf-8')
        
        if(message):
            print(f"client: {message}")

            if(find_special_char(message) and find_digit(message) and find_char(message)):
                conn_socket.send("message has special characters, digits and characters".encode('utf-8'))
                continue
            elif(find_special_char(message) and find_digit(message)):
                conn_socket.send("message has special characters and digits".encode('utf-8'))
                continue
            elif(find_char(message) and find_digit(message)):
                conn_socket.send("message has characters and digits".encode('utf-8'))
                continue
            elif(find_char(message) and find_special_char(message)):
                conn_socket.send("message has characters and special characters".encode('utf-8'))
                continue
            elif(find_char(message)):
                conn_socket.send("message has characters".encode('utf-8'))
            elif(find_digit(message)):
                conn_socket.send("message has digits".encode('utf-8'))
            elif(find_special_char(message)):
                conn_socket.send("message has special characters".encode('utf-8'))
        else:
            print("[CLIENT DISCONNECTED]")
            conn_socket.close()
