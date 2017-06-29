#python3
'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
'''
def getRow(rowIndex):
	def fact(n):
		product = 1
		while n > 0:
			product *= n
			n -= 1
		return product
		
	rowIndexList = range(rowIndex+1)
	rowList = []
	for i in rowIndexList:
		rowList.append(int(fact(rowIndex)/((fact(i)*fact(rowIndex-i)))))
	
	return rowList

if __name__ == '__main__':
	print(getRow(3))
	print(getRow(4))
	print(getRow(5))