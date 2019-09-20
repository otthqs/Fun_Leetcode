# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        p1 = head
        p2 = head.next

        head.next = None

        while p2:
            temp = p2.next
            p2.next = p1
            p1 = p2
            p2 = temp

        return p1
