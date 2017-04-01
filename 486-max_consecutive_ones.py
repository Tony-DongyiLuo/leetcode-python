#python3
'''
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''
def findMaxConsecutiveOnes(nums):
	
	if nums.count(1) == 0:
		return 0
	elif nums.count(1) == len(nums):
		return len(nums)
	
		
	zeroIndexes = [i for i, num in enumerate(nums) if num == 0]
	
	oneLengthes = []
	oneLengthes.append(zeroIndexes[0])
	for j in range(len(zeroIndexes)):
		if j != len(zeroIndexes) - 1:
			oneLengthes.append(zeroIndexes[j+1] - zeroIndexes[j] - 1)
	oneLengthes.append(len(nums) - zeroIndexes[-1] - 1)
	
	return max(oneLengthes)
	
	

if __name__ == '__main__':
	print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
	print(findMaxConsecutiveOnes([1,0,1,1,0,1]))