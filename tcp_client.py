import socket
import time

class Client:
	def __init__(self, ip, port, timeout = None):
		self.ip = ip
		self.port = port
		self.timeout = timeout

	def put(self, metric_name, metric_value, timestamp=None):
		if timestamp == None:
			self.timestamp = str(int(time.time()))
		else:
			self.timestamp = timestamp
		with socket.create_connection((self.ip, self.port), self.timeout) as self.sock:
			try:
				data = "put" + " " + metric_name + " " + str(metric_value) + " " + str(self.timestamp) + "\n"
				self.sock.sendall(data.encode("utf-8"))
				recv_data = self.sock.recv(1024)
				if not recv_data:
					raise ClientError
				if recv_data.decode('utf-8') == "error\nwrong command\n\n":
					raise ClientError
				if recv_data.decode("utf-8") == "ok\n\n":
					pass
			except Exception:
				raise ClientError


	def get(self, metric):
		self.metric = metric
		with socket.create_connection((self.ip, self.port)) as self.sock:
			try:
				data = "get" + " " + str(self.metric) + "\n"
				self.sock.sendall(data.encode("utf-8"))
				recv_data = self.sock.recv(4096).decode("utf-8")
				if not recv_data:
					raise ClientError
				if recv_data == "ok\n\n":
					res = {}
					return res
				else:
					res = {}
					data_list = recv_data[3:-2]
					data_list = data_list.split('\n')
					for i in data_list:
						i_list = i.split(' ')
						if i_list[0] in res.keys():
							res[i_list[0]].append((int(i_list[2]), float(i_list[1])))
						else:
							res[i_list[0]] = [(int(i_list[2]), float(i_list[1]))]
					return res
			except Exception:
				raise ClientError

class ClientError(Exception):
	pass

