#python3
'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''
def longestPalindrome(s):
	dictPalindrome = {}
	for char in s:
		dictPalindrome[char] = dictPalindrome.get(char, 0) + 1
	
	sumLongest = 0
	singlePoint = False
	for char in dictPalindrome:
		if dictPalindrome[char] % 2 == 0:
			sumLongest += dictPalindrome[char]
		elif dictPalindrome[char] > 2:
			sumLongest += (dictPalindrome[char] - 1)
			singlePoint = True
		else:
			singlePoint = True
			
	return (sumLongest + 1) if singlePoint else sumLongest
if __name__ == '__main__':
	print(longestPalindrome("abccccdd"))