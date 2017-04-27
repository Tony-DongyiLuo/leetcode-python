#python3
'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''
def searchInsert(nums, target):
	if target in nums:
		return nums.index(target)
	elif target < min(nums):
		return 0
	elif target > max(nums):
		return len(nums)
	else:
		for i in range(len(nums) - 1):
			if nums[i] < target and nums[i + 1] > target:
				return i + 1
		

if __name__ == '__main__':
	print(searchInsert([1,3,5,6], 5))
	print(searchInsert([1,3,5,6], 2))
	print(searchInsert([1,3,5,6], 7))
	print(searchInsert([1,3,5,6], 0))
	
			