#python3
'''
Determine whether an integer is a palindrome. Do this without extra space.
'''
def isPalindrome(x):
	
		
	origin = x
	sum = 0
	while x // 10 > 0:
		rest = x % 10
		sum = 10 * sum + rest
		x = x // 10
	sum = 10 * sum + x
	
	return origin == sum and x >= 0

if __name__ == '__main__':
	print(isPalindrome(121))
	print(isPalindrome(55))
	print(isPalindrome(848481))