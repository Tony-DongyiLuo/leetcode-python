#python3
'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        outputList = []
		def preTraverse(node):
			if node is None:
				return 
			outputList.append(node.val)
			preTraverse(node.left)
			preTraverse(node.right)
		
		preTraverse(root, k)
		for num in outputList:
			if k - num in outputList and k - num != num:
				return True
		
		return False
			