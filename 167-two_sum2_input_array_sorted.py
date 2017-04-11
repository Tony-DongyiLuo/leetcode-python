#python3
'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''
def twoSum(numbers, target):
	
	left, right = 0, len(numbers) - 1
	while left < right:
		if numbers[left] + numbers[right] < target:
			left += 1
		elif numbers[left] + numbers[right] > target:
			right -= 1
		else:
			return [left + 1, right + 1]
		

if __name__ == '__main__':
	print(twoSum([2,7,11,15],9))
	print(twoSum([2,3,4],6))
	print(twoSum([-1,0], -1))