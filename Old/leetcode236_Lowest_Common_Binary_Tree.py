# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # 这道题找的是p和q的公共祖先节点，首先用DFS搜索法找到 p 和 q的路径

        # root 表示搜寻的起点，visited是一个记录当前路径的list(初始值为[root])，node是目标节点，res是用来存储搜寻到的解的list
        def dfs(root,visited,node,res):
            # edge case
            if not root:
                return

            if root == node:
                res.append(visited[:])
                return

            # recurssion
            visited.append(root.left)
            dfs(root.left,visited,node,res)
            visited.pop()

            visited.append(root.right)
            dfs(root.right,visited,node,res)
            visited.pop()



        res = []
        dfs(root,[root],p,res)
        dfs(root,[root],q,res)

        # 提取出两个路径
        left = res[0]
        right = res[1]

        # 将较小的路径赋给left，从较小的后面开始搜索，遇到相同的node就返回得到答案
        if len(left) >= len(right):
            left,right = right,left

        for i in range(len(left)-1,-1,-1):
            if left[i] in right:
                return left[i]
