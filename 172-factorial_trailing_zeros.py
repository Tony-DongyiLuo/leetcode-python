#python3
'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
'''
def trailingZeroes(n):
	numZeros = 0
	while n > 0:
		n //= 5
		numZeros += n
	
	return numZeros

if __name__ == '__main__':
	print(trailingZeroes(95))