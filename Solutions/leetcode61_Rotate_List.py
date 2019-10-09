# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        #用双指针来进行变形
        #首先找出ListNode的长度，然后用k的值去和ListNode的长度取余，得到咱们的指针

        if not head:
            return None

        cnt = 0
        rep = head
        while rep:
            cnt += 1
            rep = rep.next

        num = k % cnt

        slow = fast = head
        for i in range(num):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        fast.next = head
        head = slow.next
        slow.next = None

        return head
