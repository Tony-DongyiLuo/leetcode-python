#python3
'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
			return []
		
		pathsList = []
		strPath = ''
		def searchTree(node, existPath):
			if node.left is None and node.right is None:
				pathsList.append((existPath + '->' + str(node.val))[2:])
				return
			else:
				newPath = existPath + '->' + str(node.val)
				if node.left is None:
					searchTree(node.right, newPath)
				elif node.right is None:
					searchTree(node.left, newPath)
				else:
					searchTree(node.left, newPath)
					searchTree(node.right, newPath)
		
		searchTree(root, strPath)
		return pathsList
				
			