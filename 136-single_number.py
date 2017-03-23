#python3
'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

def singleNumber(nums):
	return 2*sum(set(nums))-sum(nums)

if __name__ == '__main__':
	print(singleNumber([1,1,2,2,3]))
	print(singleNumber([2,2,4,4,1]))
	print(singleNumber([1]))
	