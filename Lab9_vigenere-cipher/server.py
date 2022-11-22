import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)
print(f"server listening on {HOST}, {PORT}")

def decryptVigenere(cipher_msg, key):
    orig_text = []
    for i in range(len(cipher_msg)):
        x = (ord(cipher_msg[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("".join(orig_text))

while True:
    conn_socket, addr = server.accept()
    print(f"[CONNECTED TO] : {addr}")

    while True:
        message = conn_socket.recv(1024).decode('utf-8')
        splitText = message.split("/")
        msg = splitText[0]
        key = splitText[1]

        if(message):
            print(f"\nClient : {msg}")
            deycryptedmsg = decryptVigenere(msg, key)
            print(f"[DECRYPTED MESSAGE] : {deycryptedmsg}")
            conn_socket.send(deycryptedmsg.encode('utf-8'))
        else:
            print("[CLIENT HAS DISCONNECTED!]")
            conn_socket.close()