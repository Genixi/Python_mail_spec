
l = [1,2,3,4,5]

def num_to_str(l):
	return list(map(lambda x: str(x), l))

ls = num_to_str(l)

for s in ls:
	print(s)
