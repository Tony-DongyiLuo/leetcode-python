#python3
'''
We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.
'''
def findLHS(nums):
	distinctDict = {}
	maxNum = 0
	for num in nums:
		distinctDict[num] = distinctDict.get(num,0) + 1
	
	distinctList = sorted(distinctDict.keys())
	for i in range(len(distinctList)-1):
		if distinctList[i+1] - distinctList[i] == 1:
			maxNum = max(maxNum, distinctDict.get(distinctList[i]) + distinctDict.get(distinctList[i+1]))
		
	
	return maxNum


if __name__ == '__main__':
	print(findLHS([1,3,2,2,5,2,3,7]))