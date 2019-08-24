import os
import tempfile
import random

class File():
	def __init__(self, name):
		self.name = name
		self.id = 0

	def __add__(self, other):
		tempdir = tempfile.gettempdir()
		fb = os.path.join(tempdir, 'sum' + str(random.randint(20,90)) + '.txt')
		f1 = open(self.name, 'r')
		content1 = f1.read()
		f2 = open(other.name, 'r')
		content2 = f2.read()
		f1.close()
		f2.close()
		content = content1.rstrip() + '\n' + content2.rstrip()
		fb_obj = File(fb)
		fb_obj.write(content)
		return fb_obj

	def __str__(self):
		return "{}".format(self.name)

	def write(self, text):
		with open(self.name, 'w') as f:
			f.write(text)

	def __iter__(self):
		return self

	def __next__(self):
		f = open(self.name)
		lines = f.readlines()
		if self.id == len(lines):
			raise StopIteration

		result = lines[self.id].rstrip()
		self.id += 1
		f.close()
		return result

'''
a = File('test1.txt')
b = File('test2.txt')
print(a)
for i in File('test1.txt'):
	print(i)
print(b)
for i in File('test2.txt'):
	print(i)
print(isinstance(a + b, File))
print(a + b)
for i in (a + b):
	print(i)
'''