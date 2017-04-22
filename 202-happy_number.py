#python3
'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: 
Starting with any positive integer, 
replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''
def isHappy(n):
	if n == 1 or n ==7:
		return True
	elif n in [2, 3, 4, 5, 6, 8, 9]:
		return False
	else:
		squareSum = 0
		while n != 0:
			squareSum += (n%10) ** 2
			n = n // 10
		return isHappy(squareSum)
	
if __name__ == '__main__':
	print(isHappy(19))