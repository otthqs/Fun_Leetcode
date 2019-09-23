# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        # 先将tree进行先序遍历，在调整原树结构

        if not root:
            return

        dummy = root

        stack = [dummy]

        res = []

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        res.pop(0)

        while res:
            node = res.pop(0)
            dummy.left = None
            dummy.right = TreeNode(node)
            dummy = dummy.right
