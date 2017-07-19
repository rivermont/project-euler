# Project Euler Problem 5
# Smallest Multiple

# Copyright (c) 2017 - Will Bennett
# Created under the MIT License

i = 0
n = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20] #Numbers divisible by these will be divisible by 1-10

def try_num(num, lis):
	'''
	Returns True if num is divisible by every element in lis,
	otherwise returns False.
	'''
	i = 0
	for item in lis:
		if num % item == 0:
			i += 1
	if i == len(lis):
		return True
	else:
		return False

while True:
	i += 1
	if try_num(i, n):
		print('Found number: {0}.'.format(i))
		break
