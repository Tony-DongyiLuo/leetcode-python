#python3
'''
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''
def reverseString(s):
	return s[::-1]
	
if __name__ == '__main__':
	print(reverseString('hello'))