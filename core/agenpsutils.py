import socket
import psutil
import pickle
import time

IP = '10.0.0.100'
PORT = 5000

# Create UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Instance total connection is 0
total_connections = 0

# Collect only http connections
def get_http_connections():
	container = 0
	for item in psutil.net_connections(kind='tcp'):
		if item[3][1] == 80 and item[3][0] != '0.0.0.0':
			container += 1
	return container


if __name__ == '__main__':
	print "Start sending http connections to Controller."
	# Iterating process of sending total connections
	while True:
		try:
			if total_connections != get_http_connections():
				server.connect((IP, PORT))
				total_connections = get_http_connections()
				print 'Mengirimkan %s koneksi ke %s port %s' % (total_connections, IP, PORT)
				server.send(pickle.dumps(total_connections))
		# Will stop if Interruption keyboard is detected
		except KeyboardInterrupt:
			break
		time.sleep(2)
