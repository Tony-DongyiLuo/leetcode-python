#python3
'''
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
'''
def reverseWords(s):
	splitWords = s.split(' ')
	reverseWordsList = []
	for splitWord in splitWords:
		reverseWordsList.append(splitWord[::-1])
		
	return ' '.join(reverseWordsList)

if __name__ == '__main__':
	print(reverseWords("Let's take LeetCode contest"))