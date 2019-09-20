# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(root):
            if not root:
                return 0
            return 1 + max(depth(root.left),depth(root.right))

        if not root:
            return 0


        rootres = depth(root.left)+depth(root.right)

        lres = self.diameterOfBinaryTree(root.left)
        rres = self.diameterOfBinaryTree(root.right)

        return max(rootres, lres,rres)
