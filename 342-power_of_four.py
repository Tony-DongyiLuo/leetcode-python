#python3
'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
'''
def isPowerOfFour(num):
	
	return num in [4 ** y for y in range(16)]

if __name__ == '__main__':
	print(isPowerOfFour(16))
	print(isPowerOfFour(2))