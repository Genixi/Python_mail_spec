import os
import csv

def get_car_list(csv_filename):
	with open(csv_filename) as csv_fd:
		reader = csv.reader(csv_fd, delimiter = ';')
		next(reader)
		car_list = []
		for row in reader:
			#print(row)
			if len(row) != 0 and row[0] == "car":
				#print("car choosen")
				car_list.append(Car(row[1], row[3], row[-2], row[2]))
			elif len(row) != 0 and row[0] == "truck":
				#print("track choosen")
				car_list.append(Truck(row[1], row[3], row[-2], row[-3]))
			elif len(row) != 0 and row[0] == "spec_machine":
				#print("spec_machine choosen")
				car_list.append(SpecMachine(row[1], row[3], row[-2], row[-1]))
		return car_list
		
class CarBase:
	def __init__(self, brand, photo_file_name, carrying):
		self.brand = brand
		self.photo_file_name = photo_file_name
		self.carrying = carrying

	def get_photo_file_ext(self):
		return os.path.splitext(self.photo_file_name)[1]

class Car(CarBase):
	def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
		super().__init__(brand, photo_file_name, carrying)
		self.passenger_seats_count = int(passenger_seats_count)
		self.car_type = "car"

class Truck(CarBase):
	def __init__(self, brand, photo_file_name, carrying, body_whl):
		super().__init__(brand, photo_file_name, carrying)
		self.body_whl = body_whl
		self.body_length = self.get_body_length()
		self.body_width = self.get_body_width()
		self.body_height = self.get_body_height()
		self.car_type = "truck"

	def get_body_length(self):
		if self.body_whl == "":
			return float(0)
		else:
			body_length = ""
			for s in self.body_whl:
				if s == 'x':
					break
				else:
					body_length = body_length + s
			return float(body_length)

	def get_body_width(self):
		if self.body_whl == "":
			return float(0)
		else:
			x1 = self.body_whl.find('x')
			x2 = self.body_whl.rfind('x')
			return float(self.body_whl[x1 + 1 : x2]) 


	def get_body_height(self):
		if self.body_whl == "":
			return float(0)
		else:
			x2 = self.body_whl.rfind('x')
			return float(self.body_whl[x2 + 1 :])


	def get_body_volume(self):
		return self.body_length * self.body_width * self.body_height

class SpecMachine(CarBase):
	def __init__(self, brand, photo_file_name, carrying, extra):
		super().__init__(brand, photo_file_name, carrying)
		self.extra = extra
		self.car_type = "spec_machine"

'''
cars = []
#get_car_list("coursera_week3_cars.csv")
cars = get_car_list("coursera_week3_cars.csv")
for i in cars:
	print("brand: {}, carrying: {}".format(i.brand, i.carrying))
print(cars[1].body_length)
print(cars[1].body_width)
print(cars[1].body_height)
print(cars[-1].extra)
'''