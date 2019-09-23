# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

# Edge case:
        if not root:
            return 0

# Process: 用双重递归，这里的process就是一个完整的递归方程

        def dfs(root,sum):
            if not root:
                return 0

            count = 0

            if root.val == sum:
                count += 1


            count += dfs(root.left, sum-root.val)
            count += dfs(root.right, sum-root.val)

            return count


# Recurssion:

        return dfs(root,sum) + self.pathSum(root.left,sum) + self.pathSum(root.right,sum)
