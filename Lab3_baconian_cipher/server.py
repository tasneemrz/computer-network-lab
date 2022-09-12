import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)
print(f"server listening on {HOST}, {PORT}")

lookup = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
		'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab',
		'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba',
		'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb',
		'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa', 'Z': 'bbaab'}

def decryptBaconian(message):
	decipher = ''
	i = 0
	while True:
		if(i < len(message)-4):
			substr = message[i:i + 5]
			if(substr[0] != ' '):
				decipher += list(lookup.keys())[list(lookup.values()).index(substr)]
				i += 5 

			else:
				decipher += ' '
				i += 1 
		else:
			break 
	return decipher

while True:
    conn_socket, addr = server.accept()
    print(f"[CONNECTED TO] : {addr}")

    while True:
        message = conn_socket.recv(1024).decode('utf-8')

        if(message):
            print(f"\nClient : {message}")
            deycryptedmsg = decryptBaconian(message)
            print(f"[DECRYPTED MESSAGE] : {deycryptedmsg}")
            conn_socket.send(deycryptedmsg.encode('utf-8'))

        else:
            print("[CLIENT HAS DISCONNECTED!]")
            conn_socket.close()