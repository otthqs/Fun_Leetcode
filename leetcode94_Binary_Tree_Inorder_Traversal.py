# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

#         二叉树遍历的迭代或者非迭代方式

#         res = []

#         def inorder(root):
#             if not root:
#                 return

#             inorder(root.left)
#             res.append(root.val)
#             inorder(root.right)


#         inorder(root)

#         return res


        if not root:
            return []

        stack = []
        res = []
        node = root

        while node or stack:
            if node:
                stack.append(node)
                node = node.left

            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right

        return res
