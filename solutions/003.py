# Project Euler Problem 3
# Largest prime factor

# Copyright (c) 2017 - Will Bennett
# Created under the MIT License


def get_primes(n):
	'''
	Returns a list of all the prime numbers below n.
	'''
	i = 1
	s = n**0.5 #Square root of n
	a = list(range(1, (n + 1)))
	p = []
	while i < s:
		i += 1
		print('i: ' + str(i))
		p.append(i)
		t = a[i**2-1::i] #A list of all numbers in a, starting at i^2, in increments of i
		a = set(a)
		for x in t:
			print(x)
			a.remove(x)
		a = sorted(list(a))
	return a, p

print(get_primes(100))