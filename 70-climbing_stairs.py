#python3
'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
'''
def climbStairs(n):
	stepsList = [1,2]
	if n == 1:
		return 1
	elif n == 2:
		return 2
	else:
		for i in range(2,n):
			stepsList.append(stepsList[i-1]+stepsList[i-2])
		return stepsList[n-1]

if __name__ == '__main__':
	print(climbStairs(4))
	print(climbStairs(35))
	