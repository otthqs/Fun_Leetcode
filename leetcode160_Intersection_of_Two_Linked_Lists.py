# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 第一个listnode走完后，从第二个的头开始走

        # 第二个listnode走完后，从第一个的头开始走，交点即为head

        dum1,dum2 = headA, headB

        while dum1 and dum2:
            dum1 = dum1.next
            dum2 = dum2.next

            if dum1 is None:
                dum1 = headB

                while dum1 and dum2:
                    dum1 = dum1.next
                    dum2 = dum2.next

                dum2 = headA

                while dum1 and dum2:
                    if dum1 == dum2:
                        return dum1

                    else:
                        dum1 = dum1.next
                        dum2 = dum2.next

                return None

            if dum2 is None:
                dum2 = headA

                while dum1 and dum2:
                    dum1 = dum1.next
                    dum2 = dum2.next

                dum1 = headB

                while dum1 and dum2:
                    if dum1 == dum2:
                        return dum1

                    else:
                        dum1 = dum1.next
                        dum2 = dum2.next

                return None
