# Project Euler Problem 2
# Even Fibonacci numbers

# Copyright (c) 2017 - Will Bennett
# Created under the MIT License


from functions import *

a = 0
b = 0
x = 0
i = 1

while i < 4000000:
    b = x + i
    if (x + i) % 2 == 0:
            a += x + i
    x = i
    i = b
