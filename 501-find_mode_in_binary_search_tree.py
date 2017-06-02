#python3
'''
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
		if root is None:
			return []
		midTraverseDict = {}
		def midTraverse(node):
			if node is None:
				return
			midTraverse(node.left)
			midTraverseDict[node.val] = midTraverseDict.get(node.val,0) + 1
			midTraverse(node.right)
		
		midTraverse(root)
		
		max_mode = max(midTraverseDict.values())
		modeList = [mode for mode in midTraverseDict if midTraverseDict[mode] == max_mode)]
		
		return modeList