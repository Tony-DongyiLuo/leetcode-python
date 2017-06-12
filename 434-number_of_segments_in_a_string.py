#python3
'''
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
'''
def countSegments(s):
	# if len(s) == s.count(' '):
		# return 0
		
	return len(s.split())

if __name__ == '__main__':
	print(countSegments("Of all the gin joints in all the towns in all the world,   "))
	print(countSegments("               "))