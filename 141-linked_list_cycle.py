#python
'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
		slow = fast = head
		while fast and fast.next
			fast = fast.next.next
			slow = slow.next
			if slow is fast:
				return True
		
		return False