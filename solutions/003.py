# Project Euler Problem 3
# Largest prime factor

# Copyright (c) 2017 - Will Bennett
# Created under the MIT License


from functions import *

# a = 600851475143
a = 100

x = 0
i = 2
f = []

while x < a:
	x = (a / i)
	i += 1
	if x % i == 0:
		f.append(i)
		print('Found {0}'.format(i))

print([i for i in f if is_prime(i)])

# Divisors of 600851475143:
# 71, 839, 1471, 6857, 59569, 104441, 486847, 1234169, 5753023, 10086647, 87625999, 408464633, 716151937, 8462696833
#  Y,   Y,    Y,    Y,     F,      F,      F,       F,       F,        F,        F,         F,         F,          F
