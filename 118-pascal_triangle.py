#python3
'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
def generate(numRows):
	def getFact(n):
		result = 1
		for i in range(2,n+1):
			result *= i 
		
		return result
			
	triangleList = []
	
	for numRow in range(numRows):
		rowList = []
		for item in range(numRow+1):
			rowList.append(getFact(numRow)//(getFact(item)*getFact(numRow-item)))
		triangleList.append(rowList)
	
	return triangleList

if __name__ == '__main__':
	print(generate(5))
			