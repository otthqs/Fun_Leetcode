class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        # 用数学题思维来做就是简单求组合数
        def fractional(num):
            cout = 1
            for i in range(1,num+1):
                cout *= i

            return cout

        return int(fractional(m+n-2)/(fractional(m-1)*fractional(n-1)))
