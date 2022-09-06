import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def encryptCaesar(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

while True:
    msg = input("\nYour message : ")
    s = 4
    n = len(msg)
    count = 0
        
    while count < n:
        l = msg[count]
        if (l == " "):
            print("no spaces are allowed, please re-enter")      
            msg = input("\n-> ")
            n = len(msg)
            count = 0
            continue
        count+=1

    encryptedmsg = encryptCaesar(msg, s)
    print(f"[ENCRYPTED MESSAGE] : {encryptedmsg}")
    client.send(encryptedmsg.encode('utf-8'))

    decryptedMsg = client.recv(1024).decode('utf-8')
    print(f"server : {decryptedMsg}")