# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """


        # 进行简单的中序遍历

        if not root:
            return []


        res = []
        stack = [root]

        while stack:
            temp = []
            temp_res = []
            for each in stack:
                temp_res.append(each.val)
                if each.left:
                    temp.append(each.left)

                if each.right:
                    temp.append(each.right)

            stack = temp
            res.append(temp_res)

        return res

                
