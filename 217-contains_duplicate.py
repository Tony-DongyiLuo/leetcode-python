#python3
'''
Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
'''
def containsDuplicate(nums):
	if nums:
		return len(set(nums)) != len(nums) 
	else:
		return False