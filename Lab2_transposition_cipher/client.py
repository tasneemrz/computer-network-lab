import socket
import math

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def encryptMessage(msg):
	cipher = ""
	k_indx = 0

	msg_len = float(len(msg))
	msg_lst = list(msg)
	key_lst = sorted(list(key))

	col = len(key)
	row = int(math.ceil(msg_len / col))

	fill_null = int((row * col) - msg_len)
	msg_lst.extend('_' * fill_null)

	matrix = [msg_lst[i: i + col]
			for i in range(0, len(msg_lst), col)]

	for _ in range(col):
		curr_idx = key.index(key_lst[k_indx])
		cipher += ''.join([row[curr_idx] for row in matrix])
		k_indx += 1
	return cipher

while True:
    msg = input("\nYour message : ")
    key = input("Enter key : ")

    encryptedmsg = encryptMessage(msg)
    print(f"[ENCRYPTED MESSAGE] : {encryptedmsg}")
    finalMsg = encryptedmsg + "/" + key
    client.send(finalMsg.encode('utf-8'))

    decryptedMsg = client.recv(1024).decode('utf-8')
    print(f"server : {decryptedMsg}")