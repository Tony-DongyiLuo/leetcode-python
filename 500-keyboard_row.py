#python3
'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
'''
def findWords(words):
	firstLine = 'qwertyuiop'
	secondLine = 'asdfghjkl'
	thirdLine = 'zxcvbnm'
	
	words_list = []
	for word in words:
		cal = {'first':0, 'second':0, 'third':0}
		isSameLine = True
		characters = set(word.lower())
		print(characters)
		for char in characters:
			if char in firstLine:
				if cal['second'] != 0 or cal['third'] != 0:
					isSameLine = False
					break
				cal['first'] += 1
			elif char in secondLine:
				if cal['first'] != 0 or cal['third'] != 0:
					isSameLine = False
					break
				cal['second'] += 1
			else:
				if cal['second'] != 0 or cal['first'] != 0:
					isSameLine = False
					break
				cal['third'] += 1
				
		if isSameLine:
			words_list.append(word)
	
	return words_list

if __name__ == '__main__':
	print(findWords(["Hello", "Alaska", "Dad", "Peace"]))
