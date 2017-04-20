#python3
'''
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. 
If there are less than k characters left, reverse all of them. 
If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
'''
def reverseStr(s, k):
	i = 0
	reverseList = []
	nonReverseList = []
	while i + 2 * k < len(s):
		reverseList.append(s[i:i+k])
		nonReverseList.append(s[i+k:i+2*k])
		i = i + 2 * k
		
	if i + k >= len(s):
		reverseList.append(s[i:])
		nonReverseList.append('')
	else:
		reverseList.append(s[i:i+k])
		nonReverseList.append(s[i+k:])
	
	for j in range(len(reverseList)):
		reverseList[j] = reverseList[j][::-1]
		
	return ''.join(list(map(lambda x: x[0] + x[1], zip(reverseList, nonReverseList))))

if __name__ == '__main__':
	print(reverseStr('abcdefg', 2))