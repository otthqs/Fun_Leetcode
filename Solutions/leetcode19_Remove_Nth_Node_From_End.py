# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 要求只循环一次就解决问题
        # 打算用两个指针来进行实现，当第一个指针走到最后时，第二个指针走到特定位置，把第二个指针的next，指向第二个指针的next的next
        # 题目说明了given is always be valid

        # 最好最好用哨兵头来进行，以免对原ListNode进行误改

        if not head:
            return

        dummy = ListNode(-1)

        dummy.next = head

        first = second = dummy

        i = 0

        while i < n:
            second = second.next
            i += 1

        while second.next:
            second = second.next
            first = first.next

        first.next = first.next.next

        return dummy.next
