# Project Euler
# Shared Function Library

# Copyright (c) 2017 - Will Bennett
# Created under the MIT License


def factors(num, mode):
	'''
	Modes:
	0 -> Returns a list of all factors of num.
	1 -> Returns the number of factors num has.
	2 -> Returns (list of factors of num, amount of factors)
	'''
	a = 1
	f = []
	for i in range(1, int((num / 2) + 1)):
		if num % i == 0:
			a += 1
			f.append(i)
	if mode == 0:
		return f
	elif mode == 1:
		return a
	elif mode == 2:
		return f, a

def get_primes(n):
	'''
	Returns a list of all the prime numbers up to n.
	'''
	i = 1
	s = n**0.5 #Square root of n
	a = list(range(1, (n + 1)))
	b = a
	while i < s:
		i += 1
		t = a[i**2-1::i] #A list of all numbers in a, starting at i^2, in increments of i
		b = set(b)
		for x in t:
			b.discard(x)
		b = sorted(list(b))
	return b

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

def is_completely_divisible(num, lis):
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
	return False

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

def is_prime(num):
	'''
	Returns True if num is prime,
	otherwise returns False.
	'''
	i = 1
	h = (num / 2)
	while i < h:
		i += 1
		if num % i == 0:
			return False
	return True
