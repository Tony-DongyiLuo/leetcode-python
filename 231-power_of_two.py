#python3
'''
Given an integer, write a function to determine if it is a power of two.
'''
def isPowerOfTwo(n):
	return 2 ** 31 % n == 0

