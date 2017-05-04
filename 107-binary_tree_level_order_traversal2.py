#python3
'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
		nodesDict = {}
        def preTraverse(node, depth):
			if node == None:
				return
			
			if nodesDict.get(depth) == None:
				nodesDict[depth] = [node.val]
			else:
				nodesDict[depth].append(node.val)
			preTraverse(node.left, depth+1)
			preTraverse(node.right, depth+1)
		
		preTraverse(root)
		bottomOrderList = []
		
		for i in range(max(nodesDict.keys()) + 1)[::-1]:
			bottomOrderList.append(nodesDict.get(i))
		
		return bottomOrderList
			