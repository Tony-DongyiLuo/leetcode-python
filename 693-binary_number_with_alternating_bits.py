'''
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
'''
def hasAlternatingBits(n):
	strBin = bin(n)
	for i in range(2,len(strBin)-1):
		if strBin[i] == strBin[i+1]:
			return False
	
	return True
	


if __name__ == '__main__':
	print(hasAlternatingBits(5))
	print(hasAlternatingBits(7))
	print(hasAlternatingBits(11))
	print(hasAlternatingBits(10))