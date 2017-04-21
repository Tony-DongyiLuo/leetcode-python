#python3
'''
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
'''
def isPowerOfThree(n):
	if n <= 0:
		return False
	import math
	power = math.log(n, 3)
	return str(power)[-1] == '0'

if __name__ == '__main__':
	print(isPowerOfThree(81))
	print(isPowerOfThree(51))