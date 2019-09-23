# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #定义一个helper函数来对node进行分析，返回结果是抢node的最大值和不抢node的最大值这样一个list



        def helper(root):
            #先写edge case 如果root为None则返回[0,0]
            if not root:
                return [0,0]

            # 注意用一个变量来存储left和right抢夺的信息，不要重复调用函数
            l = helper(root.left)
            r = helper(root.right)

            # 如果抢root的话，那么不能抢root的左右节点
            res0 = root.val + l[1] + r[1]

            # 如果不强root的话，可以抢root的左右节点，也可以不抢
            res1 = max(l) + max(r)

            return [res0,res1]


        return max(helper(root))

        
