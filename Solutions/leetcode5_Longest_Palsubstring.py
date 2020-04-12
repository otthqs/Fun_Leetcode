class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        #Manacher算法
        #首先处理string
        def helper(s):
            res = '^'
            for i in range(len(s)):
                res = res + '#' + s[i]
            return res + '#$'

        s_adj = helper(s)

        p = [0] * len(s_adj)
        C,R = 0,0
        for i in range(1,len(s_adj)-1):
            i_mirror = 2 * C - i
            if R > i:
                p[i] = min(p[i_mirror], R - i)
            else:
                p[i] = 0
            while s_adj[i + p[i] + 1] == s_adj[i - p[i] -1]:
                p[i] += 1
        if i + p[i] > R:
            R = i + p[i]
            C = i
        Center = 0
        Maxlen = 0
        for i in range(len(p)):
            if p[i] > Maxlen:
                Maxlen = p[i]
                Center = i
        start = (Center - Maxlen) //2
        return s[start:start+Maxlen]
            







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
