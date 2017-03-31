#python3
'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
'''
def islandPerimeter(grid):
	countOnes = []
	additionOnes = []
	internalLines = 0
	for j in range(len(grid)):
		if grid[j].count(1) > 0:
			countOnes.append(grid[j].count(1))
		if j != len(grid) - 1:
			additionOnes.append([x+y for x, y in zip(grid[j], grid[j+1])].count(2))
		
		for i in range(len(grid[j])):
			if i != len(grid[j]) - 1:
				if grid[j][i] + grid[j][i+1] == 2:
					internalLines += 1
	
	
	totalPerimeter = 4 * sum(countOnes) - 2 * sum(additionOnes) - 2 * internalLines
	return totalPerimeter

if __name__ == '__main__':
	print(islandPerimeter([[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]]))
	print(islandPerimeter([[1], [0]]))	
	print(islandPerimeter([[1, 1, 0], [0,1,1]]))
	print(islandPerimeter([[1, 1, 1], [1,0,1]]))	