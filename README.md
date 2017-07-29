# project-euler
This is a storage space for organizing my solutions to the Project Euler problems.<br>
If you do not wish to have solutions spoiled, you should probably turn around and go home.<br>
If you came here looking for solutions, take a minute to think about what you're doing, then proceed to **do them yourself please**!

[![Project Euler Profile](https://projecteuler.net/profile/r1vermont.png)](#)

--------------------

# Table of Contents

  - [project-euler](#project-euler)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Problems](#problems)
    - [001](#001---multiples-of-3-and-5)
    - [002](#002---even-fibonacci-numbers)
	- [003](#003---largest-prime-factor)
    - [004](#004---largest-palindrome-product)
    - [005](#005---smallest-multiple)
	- [006](#006---sum-square-difference)
	- [012](#012---highly-divisible-triangular-number)
	- [013](#013---large-sum)
  - [Functions](#functions)
    - [count_divisors](#count-divisors)
	- [get_primes](#get_primes)
	- [get_triangle](#get_triangle)
	- [is_completely_divisible](#is-completely-divisible)
	- [is_palindrome](#is-palindrome)
  - [Questions](#questions)

# About
Project Euler is a series of a few hundred programming problems designed to challenge and force learning.<br>
The complexity of the problems scales very rapidly, and the hard ones challenge even the best of coders.

I needed a new project to work on, so I have begun going through the problems on my own.<br>


# Problems

## 001 - Multiples of 3 and 5
Python - [`001.py`](https://github.com/rivermont/project-euler/blob/master/solutions/001.py) - 1 line

## 002 - Even Fibonacci numbers
Python - [`002.py`](https://github.com/rivermont/project-euler/blob/master/solutions/002.py) - 10 lines

## 003 - Largest Prime Factor
Python - [`003.py`](https://github.com/rivermont/project-euler/blob/master/solutions/003.py)

## 004 - Largest palindome product
Python - [`004.py`](https://github.com/rivermont/project-euler/blob/master/solutions/004.py) - 15 lines

## 005 - Smallest multiple
Python - [`005.py`](https://github.com/rivermont/project-euler/blob/master/solutions/005.py) - 16 lines

## 006 - Sum square difference
Python - [`006.py`](https://github.com/rivermont/project-euler/blob/master/solutions/006.py) - 13 lines


## 012 - Highly divisible triangular number
Python - [`012.py`](https://github.com/rivermont/project-euler/blob/master/solutions/012.py) - 24 lines

## 013 - Large sum
Python - [`013.py`](https://github.com/rivermont/project-euler/blob/master/solutions/013.py) - 6 lines<br>
My original thought was to use `threading` and calculate the numbers simultaneously, but it turned out they could just be bruteforced in a second.


# Functions

## `count_divisors`
Returns the number of divisors/factors that `num` has.

> count_divisors(num)

## `get_primes`
Returns a list of all the prime numbers up to `n`.

> get_primes(n)

## `get_triangle`
Returns the `num`-th triangle number.

> get_triangle(num)

## `is_completely_divisible`
Returns `True` if `num` is divisible by every element in `lis`, otherwise returns `False`.

> is_completely_divisible(num, lis)

## `is_palindrome`
Returns `True` if `num` is a palindrome, otherwise returns `False`.


# Questions
I understand that Project Euler do not like it when solutions are shared online, however that is not my intent.<br>
I created this repo to organize my own code for myself, not to share it with people looking for solutions (hence the warning at the top).<br>
