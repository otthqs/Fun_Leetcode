class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root:
            return self.isSymmetricTree(root.left,root.right)

        return True

    def isSymmetricTree(self,p,q):
        if p and q:
            return p.val == q.val and self.isSymmetricTree(p.left,q.right) and self.isSymmetricTree(p.right,q.left)

        return p == q
