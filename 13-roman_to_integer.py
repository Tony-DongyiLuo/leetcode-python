#python3
'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''
def romanToInt(s):
	dictRoman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
	romanInt = 0
	for i in range(len(s) - 1):
		if dictRoman.get(s[i]) < dictRoman.get(s[i+1]):
			romanInt -= dictRoman.get(s[i])
		else:
			romanInt += dictRoman.get(s[i])
	romanInt += dictRoman.get(s[-1])
		
	
	return romanInt

if __name__ == '__main__':
	print(romanToInt("MCMXCVI"))
		