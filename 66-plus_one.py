#python3
'''
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
'''
def plusOne(digits):
	
	strNum = ''
	for digit in digits:
		strNum = strNum + str(digit)
	num = int(strNum) + 1
		
	numDigits = str(num)
		
	digitsList = [int(numDigit) for numDigit in numDigits]
		
	return digitsList

if __name__ == '__main__':
	print(plusOne([1,0,1]))
	#print(plusOne([0]))