#python3
'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''
def maxSubArray(nums):
	curSum = maxSum = nums[0]
	for num in nums[1:]:
		curSum = max(num, curSum + num)
		maxSum = max(maxSum, curSum)
	
	return maxSum

if __name__ == '__main__':
	print(maxSubArray([-2,1]))
	print(maxSubArray([-1]))
	print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))