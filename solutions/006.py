# Project Euler Problem 6
# Sum square difference

# Copyright (c) 2017 - Will Bennett
# Created under the MIT License

from functions import *

i = 0
m = 0 #Sum of the squares
n = 0 #Square of the sum

while i < 100:
	i += 1
	print(i)
	m += i**2
	n += i

n = n**2
print('Sum of the squares: {0}'.format(m))
print('Square of the sum: {0}'.format(n))

a = n - m

print('Difference: {0}'.format(a))
