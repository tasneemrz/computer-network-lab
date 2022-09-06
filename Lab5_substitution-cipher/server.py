import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)
print(f"server listening on {HOST}, {PORT}")

key = input("Enter key for security : ")

def decrypt(msg, key):
    key = int(key)
    res = ""
    for i in msg:
        res += chr((ord(i)-key+128)%128)
    return res

while True:
    conn_socket, addr = server.accept()
    print(f"[CONNECTED TO] : {addr}")

    while True:
        msg = conn_socket.recv(1024).decode()
        
        print("Client : ", msg)
        decrypted_msg = decrypt(msg,int(key))
        if decrypted_msg == ";":
            break
        
        conn_socket.send(bytes(decrypted_msg,'utf-8'))
            