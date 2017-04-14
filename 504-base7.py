#python3
'''
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
'''
def convertToBase7(num):
	if num == 0:
		return "0"
	newNum = abs(num)
	base7Str = ""
	while newNum != 0:
		
		base7Str = str(newNum % 7) + base7Str
		newNum = int(newNum / 7)
		
		
	return ("-" + base7Str) if num < 0 else base7Str


if __name__ == '__main__':
	print(convertToBase7(100))
	print(convertToBase7(-7))
	print(convertToBase7(9))