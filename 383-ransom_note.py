#python3
'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; 
otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''

def canConstruct(ransomNote, magazine):
	for char in set(ransomNote):
		if ransomNote.count(char) > magazine.count(char):
			return False
	return True
	
if __name__ == '__main__':
	print(canConstruct("a","b"))
	print(canConstruct("aa","ab"))
	print(canConstruct("aa","aab"))