# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 要对ListNode进行排序，选择merge排序的方法
        # 进行第一步：拆分；第二步：排序

        if not head or not head.next:
            return head

        left,right = self.spl(head)
        return self.merge(self.sortList(left),self.sortList(right))


    def merge(self,head1,head2):
        dummy = root = ListNode(-1)
        while head1 and head2:
            if head1.val <= head2.val:
                dummy.next = head1
                dummy = dummy.next
                head1 = head1.next

            else:
                dummy.next = head2
                dummy = dummy.next
                head2 = head2.next

        if head1:
            dummy.next = head1

        else:
            dummy.next = head2

        return root.next

    def spl(self,head):

        if head and head.next:
            slow = fast = head
            while fast and fast.next:
                pre = slow
                fast = fast.next.next
                slow = slow.next

            pre.next = None
            return head, slow

        else:
            return None,None
    
