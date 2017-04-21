#python3
'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
def addStrings(num1, num2):
	tenDigits = '0123456789'
	number1 = 0
	number2 = 0
	lenNum1 = len(num1)
	lenNum2 = len(num2)
	
	for i in range(lenNum1):
		number1 += tenDigits.index(num1[i]) * (10 ** (lenNum1 - i - 1))
	
	for j in range(lenNum2):
		number2 += tenDigits.index(num2[j]) * (10 ** (lenNum2 - j - 1))
	
	return str(number1+number2)

if __name__ == '__main__':
	print(addStrings('9', '99'))