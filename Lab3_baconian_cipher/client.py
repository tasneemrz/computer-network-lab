import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

lookup = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
		'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab',
		'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba',
		'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb',
		'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa', 'Z': 'bbaab'}

def encryptBaconian(message):
	cipher = ''
	for letter in message:
		if(letter != ' '):
			cipher += lookup[letter]
		else:
			cipher += ' '
	return cipher

while True:
    msg = input("\nYour message : ")

    encryptedmsg = encryptBaconian(msg.upper())
    print(f"[ENCRYPTED MESSAGE] : {encryptedmsg}")
    client.send(encryptedmsg.lower().encode('utf-8'))

    decryptedMsg = client.recv(1024).decode('utf-8')
    print(f"server : {decryptedMsg}")