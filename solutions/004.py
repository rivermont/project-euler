# Project Euler Problem 4
# Largest palindrome product

# Copyright (c) 2017 - Will Bennett
# Created under the MIT License


from functions import *

p = set([])

for m in range(100, 1000):
	for n in range(100, 1000):
		if is_palindrome(m * n):
			p.add(m * n)

p = list(p)
p.sort()
print(p[-1])
