#python3
'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
'''
def getSum(a, b):
	MAX = 0x7FFFFFFF
	MIN = 0x80000000
	
	mask = 0xFFFFFFFF
	while b != 0:
		# ^ get different bits and & gets double 1s, << moves carry
		a, b = (a ^ b) & mask, ((a & b) << 1) & mask
	
	return a if a <= MAX else ~(a ^ mask)

if __name__ == '__main__':
	print(getSum(1, 2))
	print(getSum(5, 5))
	print(getSum(-1, 2))
	print(getSum(-1, -2))
	print(getSum(-2, -2))
	print(getSum(3, 4))
	print(getSum(3, 0))
	print(getSum(-2, 0))