#python3
'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
		valDict = {}
		def preTraverse(node,depth):
			if node is None:
				return
			if valDict.get(depth):
				valDict[depth].append(node.val)
			else:
				valDict[depth] = [node.val]
			preTraverse(node.left,depth+1)
			preTraverse(node.right,depth+1)
			
		preTraverse(root,0)
		
		averageList = []
		for i in range(max(valDict.keys())+1):
			averageList.append(sum(valDict[i])/float(len(valDict[i])))
		
		return averageList