# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 定义快慢指针来相遇，当快指针遇上慢指针的时候，快指针从头开始一步一步走，慢指针继续走，下一次相遇就是开头
        #  for else 是指 for循坏中没有任何收获执行else； while else是指while条件不满足的时候，执行else语句
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next

                return slow



        return None
