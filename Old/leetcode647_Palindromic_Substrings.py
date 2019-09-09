class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 定义helper函数来寻找以i,j位置为中心的字符串，是不是回文
        # 用两个循环来寻找回文数目，第一个循环找不同中心的回文，第二个循环找同一个中心的回文

        def helper(s,i,j):
            cout = 0
            while i>=0 and j <len(s):
                if s[i] == s[j]:
                    cout += 1
                    i -= 1
                    j += 1

                else:break

            return cout

        cout = 0

        for i in range(len(s)):
            cout += helper(s,i,i)

        for i in range(len(s)-1):
            cout += helper(s,i,i+1)

        return cout
