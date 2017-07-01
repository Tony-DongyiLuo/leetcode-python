#python3
'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

'''
def removeDuplicates(nums):
	if not nums:
		return 0
	
	i, j = 1,1
	while j < len(nums):
		if nums[i-1] != nums[j]:
			nums[i] = nums[j]
			i += 1
		j += 1
	
	return i
	
	
		
if __name__ == '__main__':
	print(removeDuplicates([1,1,1]))