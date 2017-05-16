#python3
'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''

'''
f(0) = nums[0]
f(1) = max(num[0], num[1])
f(k) = max( f(k-2) + nums[k], f(k-1) )
'''
def rob(nums):
	previousSum, currentSum = 0,0
	for num in nums:
		previousSum, currentSum = currentSum, max(previousSum+num, currentSum)
	
	return currentSum



if __name__ == '__main__':
	print(rob([1,1]))