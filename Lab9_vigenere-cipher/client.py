import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def encryptVigenere(text, key):
    cipher_text = []
    for i in range(len(text)):
        x = (ord(text[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("".join(cipher_text))

def generateKey(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return(key)
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return("".join(key))

while True:
    msg = input("\nYour message : ")
    keyword = "lab"
    key = generateKey(msg, keyword)

    encryptedmsg = encryptVigenere(msg, key)
    finalMsg = encryptedmsg + "/" + key

    client.send(finalMsg.encode('utf-8'))
    decryptedMsg = client.recv(1024).decode('utf-8')
    print(f"server : {decryptedMsg}")
    