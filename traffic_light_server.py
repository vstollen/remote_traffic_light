import socket

from gpiozero import LED
from time import sleep

red = LED(14)
yellow = LED(15)
green = LED(18)

state = 'UNKNOWN'
red.on()
yellow.on()
green.on()

# Create TCP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a port
server_adress = ('localhost', 10000)
print('Starting up on %s port %s' % server_adress)
sock.bind(server_adress)

# Listen for connections
sock.listen(1)

while True:
	print('Waiting for a connection')
	connection, client_adress = sock.accept()

	try:
		print('connection from ', client_adress)

		while True:
			data = connection.recv(16)
			print('received %s' % data)
			
			if not data:
				break

			if data == 'GREEN':
				if state == 'GREEN':
					break

				state = 'GREEN'
				
				yellow.on()
				sleep(1)
				
				red.off()
				yellow.off()
				green.on()
			
			elif data == 'RED':
				if state == 'RED':
					break

				state = 'RED'

				green.off()
				yellow.on()
				sleep(1)

				yellow.off()
				red.on()
			else:
				print('Unknown Command')
				state = 'ERROR'
				green.on()
				yellow.on()
				red.on()

	finally:
		connection.close()
