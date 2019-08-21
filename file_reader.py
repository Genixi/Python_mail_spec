class FileReader():
	def __init__(self, path):
		self.path = path

	def read(self):
		try:
			with open(self.path) as f:
				content = f.read()
		except FileNotFoundError:
			return ("")
		else:
			return (content)

