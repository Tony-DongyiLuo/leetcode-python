#python3
'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''
def missingNumber(nums):
	length = len(nums)
	return int(length * (length + 1) / 2) - sum(nums)
	
if __name__ == '__main__':
	print(missingNumber([0,1,3]))