#python3
'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''
def firstUniqChar(s):
	oneTimeIndexList = []
	for char in set(s):
		if s.count(char) == 1:
			oneTimeIndexList.append(s.index(char))
	
	if oneTimeIndexList:
		return min(oneTimeIndexList)
	else:
		return -1


if __name__ == '__main__':
	print(firstUniqChar("leetcode"))
	print(firstUniqChar("loveleetcode"))
	print(firstUniqChar("aa"))