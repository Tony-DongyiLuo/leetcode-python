#python3
'''
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
'''
def numberOfBoomerangs(points):
	sumBoomerangs = 0
	for point in points:
		distDict = {}
		for newPoint in points:
			x = point[0] - newPoint[0]
			y = point[1] - newPoint[1]
			distDict[x * x + y * y] = 1 + distDict.get(x * x + y * y, 0)
		
		for dist in distDict:
			sumBoomerangs += distDict[dist] * (distDict[dist] - 1)

	return sumBoomerangs

if __name__ == '__main__':
	print(numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]]))
	print(numberOfBoomerangs([[1,1],[2,2],[3,3]]))