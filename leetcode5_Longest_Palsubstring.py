class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # 从一个字符的中间开始到两边，如果每一个字符都相等话，那么它就是一个回文
        # 定义helper函数来实现这个功能

        def helper(i,j):
            while i >=0 and j <= len(s)-1:
                if s[i] == s[j]:
                    i -= 1
                    j += 1
                else:
                    break

            return  s[i+1:j]

        if not s or s == s[::-1]:
            return s

        big = 0

        res = ""

        for i in range(len(s)):
            temp = helper(i,i)
            if big <= len(temp):
                big = len(temp)
                res = temp

        for i in range(len(s)-1):
            temp = helper(i,i+1)
            if big <= len(temp):
                big = len(temp)
                res = temp


        return res
