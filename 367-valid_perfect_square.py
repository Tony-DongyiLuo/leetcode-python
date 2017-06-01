#python3
'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
'''
def isPerfectSquare(num):
	root = num
	while root * root > num:
		root = (root + num // root) // 2
	
	return root * root == num

if __name__ == '__main__':
	print(isPerfectSquare(16))
	print(isPerfectSquare(14))

