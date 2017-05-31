#python3
'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
'''
def reverseVowels(s):
	vowels = 'aeiouAEIOU'
	sList = list(s)
	vowelList = [char for char in sList if char in vowels]
	for i in range(len(sList)):
		if sList[i] in vowels:
			sList[i] = vowelList.pop()
	
	return ''.join(sList)

if __name__ == '__main__':
	print(reverseVowels('hello'))
	print(reverseVowels('aA'))