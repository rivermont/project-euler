# Project Euler Problem 5
# Smallest Multiple

# Copyright (c) 2017 - Will Bennett
# Created under the MIT License


from functions import *

i = 0
n = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20] #Numbers divisible by these will be divisible by 1-10

while True:
	i += 1
	if is_completely_divisible(i, n):
		print('Found number: {0}.'.format(i))
		break
