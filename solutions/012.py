# Project Euler Problem 12
# Highly divisible triangular number

# Copyright (c) 2017 - Will Bennett
# Created under the MIT License


from functions import *

n = 0

while True:
	n += 1
	tri = get_triangle(n)
	divs = count_divisors(tri)
	print('{0}: {1}: {2}'.format(n, tri, divs))
	if divs >= 500:
		print('Found {0}'.format(tri))
		break
