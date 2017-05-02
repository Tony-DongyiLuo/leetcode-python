#python3
'''
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
'''
def isUgly(num):
	if num <= 0:
		return False
	if num == 1:
		return True
	
	if (num % 5 != 0 and num % 2 != 0 and num % 3 != 0):
		return False
		
	if num % 2 == 0:
		return isUgly(num // 2)
	if num % 3 == 0:
		return isUgly(num // 3)
	if num % 5 == 0:
		return isUgly(num // 5)

if __name__ == '__main__':
	print(isUgly(1))
	print(isUgly(6))
	print(isUgly(8))
	print(isUgly(14))