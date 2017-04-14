#python3
'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
'''
def isAnagram(s, t):
	if len(s) != len(t):
		return False
	for i in set(t):
		if t.count(i) > s.count(i):
			return False
	return True

if __name__ == '__main__':
	print(isAnagram("anagram", "nagaram"))
	print(isAnagram("rat", "car"))
	print(isAnagram("ab", "a"))