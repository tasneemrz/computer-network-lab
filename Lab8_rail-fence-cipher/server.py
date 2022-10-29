import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)
print(f"server listening on {HOST}, {PORT}")

def decryptRailFence(cipher_msg, key):
	rail = [['\n' for i in range(len(cipher_msg))] for j in range(key)]

	dir_down = None
	row, col = 0, 0

	for i in range(len(cipher_msg)):
		if row == 0:
			dir_down = True
		if row == key - 1:
			dir_down = False

		rail[row][col] = '*'
		col += 1
		
		if dir_down:
			row += 1
		else:
			row -= 1

	index = 0
	for i in range(key):
		for j in range(len(cipher_msg)):
			if ((rail[i][j] == '*') and
			(index < len(cipher_msg))):
				rail[i][j] = cipher_msg[index]
				index += 1

	result = []
	row, col = 0, 0
	for i in range(len(cipher_msg)):

		if row == 0:
			dir_down = True
		if row == key-1:
			dir_down = False

		if (rail[row][col] != '*'):
			result.append(rail[row][col])
			col += 1

		if dir_down:
			row += 1
		else:
			row -= 1
	return("".join(result))

while True:
    conn_socket, addr = server.accept()
    print(f"[CONNECTED TO] : {addr}")

    while True:
        k = 3
        message = conn_socket.recv(1024).decode('utf-8')

        if(message):
            print(f"\nClient : {message}")
            deycryptedmsg = decryptRailFence(message, 3)
            print(f"[DECRYPTED MESSAGE] : {deycryptedmsg}")

        else:
            print("[CLIENT HAS DISCONNECTED!]")
            conn_socket.close()
