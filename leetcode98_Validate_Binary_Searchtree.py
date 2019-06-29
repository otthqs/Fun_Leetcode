# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # 二叉搜索树的中序遍历是递增序列，用迭代方式进行中序遍历


        res = []

        # 迭代方式的中序遍历
        # def inorder(root):
        #     if not root:
        #         return
        #
        #     inorder(root.left)
        #     res.append(root.val)
        #     inorder(root.right)
        #
        # inorder(root)

        # 非迭代方式的中序遍历：

        node = root
        stack = []

        while node or stack:
            if node:
                stack.append(node)
                node = node.left

            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right


        for i in range(len(res)-1):
            if res[i] >= res[i+1]:
                return False

        return True
