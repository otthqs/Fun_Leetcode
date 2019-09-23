class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        # 利用迭代来进行generate valid parentheses

        res = []

        # s为当下的括号情况，初始情况为"",l为左括号的数目，r为右括号的数目
        def helper(s,l,r):
            if len(s) == 2*n:
                res.append(s)
                return

        # 如果长度不够的话，就先加左边
            if l < n:
                helper(s+"(",l+1,r)

        # 如果左括号的长度比右括号多，可以加右括号
            if l > r:
                helper(s+")",l,r+1)

        helper("",0,0)

        return res
