import sys

digit_string = sys.argv[1]
sum = 0
for s in digit_string:
	sum = sum + int(s)

print(sum)