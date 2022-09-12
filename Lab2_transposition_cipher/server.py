import socket
import math

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)
print(f"server listening on {HOST}, {PORT}")

def decryptMessage(cipher):
	msg = ""
	k_indx = 0
	msg_indx = 0
	msg_len = float(len(cipher))
	msg_lst = list(cipher)

	col = len(key)
	row = int(math.ceil(msg_len / col))
	key_lst = sorted(list(key))

	dec_cipher = []
	for _ in range(row):
		dec_cipher += [[None] * col]

	for _ in range(col):
		curr_idx = key.index(key_lst[k_indx])

		for j in range(row):
			dec_cipher[j][curr_idx] = msg_lst[msg_indx]
			msg_indx += 1
		k_indx += 1

	try:
		msg = ''.join(sum(dec_cipher, []))
	except TypeError:
		raise TypeError("This program cannot", "handle repeating words.")

	null_count = msg.count('_')

	if null_count > 0:
		return msg[: -null_count]
	return msg

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
            deycryptedmsg = decryptMessage(msg)
            print(f"[DECRYPTED MESSAGE] : {deycryptedmsg}")
            conn_socket.send(deycryptedmsg.encode('utf-8'))

        else:
            print("[CLIENT HAS DISCONNECTED!]")
            conn_socket.close()