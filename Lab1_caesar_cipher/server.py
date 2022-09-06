import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)
print(f"server listening on {HOST}, {PORT}")

def decryptCaesar(cipher_text, s):
    result = ""
    for i in range(len(cipher_text)):
        char = cipher_text[i]

        if (char.isupper()):
            result += chr((ord(char) + 26 - s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + 26 - s - 97) % 26 + 97)
    return result

while True:
    conn_socket, addr = server.accept()
    print(f"[CONNECTED TO] : {addr}")

    while True:
        message = conn_socket.recv(1024).decode('utf-8')
        s = 4

        if(message):
            print(f"\nClient : {message}")
            deycryptedmsg = decryptCaesar(message, s)
            print(f"[DECRYPTED MESSAGE] : {deycryptedmsg}")
            conn_socket.send(deycryptedmsg.encode('utf-8'))

        else:
            print("[CLIENT HAS DISCONNECTED!]")
            conn_socket.close()