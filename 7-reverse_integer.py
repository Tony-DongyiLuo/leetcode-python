#!usr/bin/env python3
#-*- coding: utf-8 -*-
'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.

'''
def reverse(x):
	"""
	:type x: int
	:rtype: int
	"""
	new_num = 0
	if x < 0 and x > -2147483647:
		new_num = -(int(str(-x)[-1::-1]))
		if new_num > -2147483647:
			return new_num
		else:
			return 0
	elif x > 0 and x < 2147483647:
		new_num = int(str(x)[-1::-1])
		if new_num < 2147483647:
			return new_num
		else:
			return 0
	else:
		return 0


print (reverse(-123))
print (reverse(2334))
print (reverse(120))