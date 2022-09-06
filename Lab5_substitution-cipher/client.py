import socket

HOST = '192.168.1.9'
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def encrypt(msg, key):
    key = int(key)
    res = ""
    for i in msg:
        res += chr((ord(i)+key)%128)
    return res

while True:
    msg = input('Enter your message : ')
    key = input('Enter your key : ')
    encrypted_msg = encrypt(msg,int(key))
    print("Cipher Text send to Server : ",encrypted_msg)
    if msg==";" :
        client.close()
        break
    
    client.send(bytes(encrypted_msg,'utf-8'))
    decrypted_msg = client.recv(1024).decode()
    print(f"Decrypted msg : {decrypted_msg}")
