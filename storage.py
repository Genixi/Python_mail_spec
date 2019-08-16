import argparse
import os
import tempfile
import json


parser = argparse.ArgumentParser()
parser.add_argument("--key", type = str)
parser.add_argument("--val", type = str)
args = parser.parse_args()

if args.key and args.val:
	storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
	if os.path.exists(storage_path):
		with open(storage_path, "r") as f:
			data = json.load(f)
			if args.key in data.keys():
				data[args.key].append(args.val)
				#print("case4")
				with open(storage_path, "w") as f:
					json.dump(data,f)
			else:
				#print("case5")
				data[args.key] = [args.val]
				with open(storage_path, "w") as f:
					json.dump(data, f)
	else:
		with open(storage_path, "w") as f:
			#print("case3")
			json.dump({args.key : [args.val]}, f)

else:
	storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
	if os.path.exists(storage_path):
		with open(storage_path, "r") as f:
			data = json.load(f)
			if args.key in data.keys():
				print(', '.join(data[args.key]))
			else:
				#print("case1")
				print("None")
	else:
		#print("case2")
		print("None") 




