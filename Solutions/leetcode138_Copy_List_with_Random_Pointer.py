"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        def copyList(head):

            if not head:
                return None

            if head in refDict:
                return refDict[head]

            dp_head = Node(head.val, None, None)

            refDict[head] = dp_head

            # deep copy
            dp_head.random = copyList(head.random)
            dp_head.next = copyList(head.next)


            return dp_head

        refDict = {}

        return copyList(head)
