import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_adress = ('localhost', 10000)
print('Connecting to %s on port %s' % server_adress)
sock.connect(server_adress)

try:
	message = sys.argv[1]
	print('Sending: ', message)
	sock.sendall(message)

finally:
	print('Closing Socket')
	sock.close()
