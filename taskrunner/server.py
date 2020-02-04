import socket
import threading
import json

class ThreadedServer:
	def __init__(self, config):
		self.host = config["host"]
		self.port = config["port"]
		self.timeout = config["timeout"]
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
		self.sock.bind((self.host, self.port))
		print("Starting a server on %s:%s" % (self.host, self.port))

	def listen(self):
		self.sock.listen()
		while True:
			client, address = self.sock.accept()
			client.settimeout(self.timeout);
			threading.Thread(target = self.listenToClient, args = (client, address)).start()

	def listenToClient(self, client, address):
		size = 1024
		while True:
			try:
				data = client.recv(size)
				if data:
					print("Data received: %s" % data)
					client.send(data)
				else:
					raise error('Client disconnected')
			except:
				client.close()
				return False


if __name__ == "__main__":
	with open("config.cfg") as config_file:
		config = json.load(config_file);
	ThreadedServer(config).listen()
