# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 用迭代的方法来进行建树

        # 先写edge case：
        # 在这里return None能保证连续和一致，所以即使接下来是return root,这里也可以return None
        if not preorder:
            return None

        # 先序遍历的第一个节点是目前的根节点
        # 中序遍历根节点之前的节点是左子树的节点
        node = preorder[0]

        root = TreeNode(node)

        m = inorder.index(node)

        # 先序遍历是：根，左，右，所以在preorder[0]之后剩余的元素，先是其左子树，再是其右子树
        root.left = self.buildTree(preorder[1:m+1],inorder[0:m])

        # 中序遍历是：在目前根左边的都是左子树，根右边的是右子树
        root.right = self.buildTree(preorder[m+1:],inorder[m+1:])

        return root
