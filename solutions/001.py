# Project Euler Problem 1
# Multiples of 3 and 5

# Copyright (c) 2017 - rivermont
# Created under the MIT License

x = 0
for i in range(0, 1000):
	if i % 5 == 0 or i % 3 == 0:
		x += i

#One-liner
x = sum([i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0])

#Minimum characters: 51
# sum([i for i in range(1,1000) if i%3==0 or i%5==0])