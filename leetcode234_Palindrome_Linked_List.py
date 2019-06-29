# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: 'ListNode') -> 'bool':
        #将原ListNode分解为两部段，前半段和后半段，将后半段翻转，来和前半段进行对比，对比一致则为True


        def rev(head):
            if not head or head.next is None:
                return head

            p,q = head, head.next

            while q:
                temp = q.next
                q.next = p
                p = q
                q = temp
            head.next = None
            return p

        slow, fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        new_head = rev(slow)

        while new_head:
            if new_head.val == head.val:
                head = head.next
                new_head = new_head.next

            else:
                return False

        return True
