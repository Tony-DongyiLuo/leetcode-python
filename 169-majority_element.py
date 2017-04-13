#python3
'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''
def majorityElement(nums):
	"""
        :type nums: List[int]
        :rtype: int
        """
	
	for num in set(nums):
		if nums.count(num) > len(nums)/2:
			return num