import socket

HOST = '192.168.1.9'
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def encryptRailFence(text, key):

	rail = [['\n' for i in range(len(text))] for j in range(key)]
	
	dir_down = False
	row, col = 0, 0
	
	for i in range(len(text)):
		if (row == 0) or (row == key - 1):
			dir_down = not dir_down
		
		rail[row][col] = text[i]
		col += 1

		if dir_down:
			row += 1
		else:
			row -= 1

	result = []
	for i in range(key):
		for j in range(len(text)):
			if rail[i][j] != '\n':
				result.append(rail[i][j])
	return ("".join(result))
    

while True:
    msg = input("Your message : ")
    key = 3

    encryptedmsg = (encryptRailFence(msg, key)).encode('utf-8')
    client.send(encryptedmsg)
