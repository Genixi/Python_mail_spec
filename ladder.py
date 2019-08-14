import sys
num_steps = int(sys.argv[1])
for i in range(num_steps):
	for k in range(num_steps - i - 1):
		print(' ', end='')
	for j in range(i + 1):
		print('#', end='')
	print('')