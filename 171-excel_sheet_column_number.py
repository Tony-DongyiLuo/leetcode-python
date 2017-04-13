#python3
'''
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
'''
def titleToNumber(s):
	UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	
	s = s[::-1]
	columnNum = 0
	for i in range(len(s)):
		columnNum += (26 ** i) * (UPPERCASE.index(s[i]) + 1) 

	return columnNum
	
if __name__ == '__main__':
	print(titleToNumber("A"))
	print(titleToNumber("AA"))
	print(titleToNumber("BA"))