# Project Euler Problem 12
# Highly divisible triangular number

# Copyright (c) 2017 - Will Bennett
# Created under the MIT License

def get_triangle(num):
	'''
	Returns the num-th triangle number.
	'''
	i = 0
	a = 0
	while i < num:
		i += 1
		a += i
	return a

def count_divisors(num):
	x = 1
	for i in range(1, int((num / 2) + 1)):
		if num % i == 0:
			x += 1
	return x

n = 0
while True:
	n += 1
	tri = get_triangle(n)
	divs = count_divisors(tri)
	print('{0}: {1}: {2}'.format(n, tri, divs))
	if divs >= 200:
		print('Found {0}'.format(tri))
		break
