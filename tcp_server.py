import asyncio

class Storage():
	def __init__(self):
		self.storage = {}

	def put(self, data):
		if data[1] in self.storage.keys():
			if (int(data[3]), float(data[2])) not in self.storage[data[1]]:
				self.storage[data[1]].append((int(data[3]), float(data[2])))
				self.storage[data[1]].sort()
		else:
			self.storage[data[1]] = [(int(data[3]), float(data[2]))]
		return "ok\n\n"

	def get(self, data):
		if data[1] in self.storage.keys():
			res = "ok\n"
			for i in self.storage[data[1]]:
				res = res + str(data[1]) + " " + str(i[1]) + " " + str(i[0]) + "\n"
			res = res + "\n"
			return res
		elif data[1] == "*":
			res = "ok\n"
			for k in self.storage.keys():
				for i in self.storage[k]:
					res = res + str(k) + " " + str(i[1]) + " " + str(i[0]) + "\n"
			res = res + "\n"
			return res
		else:
			return "ok\n\n"

storage = Storage()

class ClientServerProtocol(asyncio.Protocol):

	def connection_made(self, transport):
		self.transport = transport

	def data_received(self, data):
		#подготовка ответа об обработке данных
		resp = self.process_data(data.decode("utf-8"))
		#отправка ответа об обработке данных
		self.transport.write(resp.encode("utf-8"))

	def process_data(self, data):
		data = data[:-1].split(' ')
		if data[0] == "put":
			storage.put(data)
			return "ok\n\n"
		elif data[0] == "get":
			res = storage.get(data)
			return res
		else:
			res = "error\nwrong command\n\n"
			return res

def run_server(host, port):
	loop = asyncio.get_event_loop()
	coro = loop.create_server(ClientServerProtocol, host, int(port))
	server = loop.run_until_complete(coro)

	try:
		loop.run_forever()
	except KeyboardInterrupt:
		pass

	server.close()
	loop.run_until_complete(server.wait_closed())
	loop.close()

#if __name__ == '__main__':
#	run_server("127.0.0.1", 8181)
