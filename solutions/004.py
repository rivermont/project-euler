# Project Euler Problem 4
# Largest palindrome product

# Copyright (c) 2017 - Will Bennett
# Created under the MIT License


p = set([])

def is_palindrome(num):
	'''
	Returns True if num is a palindrome,
	otherwise returns False.
	'''
	l = []
	for i in str(num):
		l.append(i)
	if l == l[::-1]:
		return True
	return False

for m in range(100, 1000):
	for n in range(100, 1000):
		if is_palindrome(m * n):
			p.add(m * n)

p = list(p)
p.sort()
print(p[-1])
