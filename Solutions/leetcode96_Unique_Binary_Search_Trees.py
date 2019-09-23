class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """


        # catlan数组的计算和应用
        # dp[n] = dp[1]*dp[n-1] + d[2]*dp[n-2] + dp[3]*dp[n-3]

        #或者理解成为一道动态规划题
        if n==0 or n == 1:
            return n

        dp = [1,1]

        for i in range(2,n+1):
            temp = 0
            for j in range(i):
                temp += dp[j] * dp[i-j-1]

            dp.append(temp)

        return dp[-1]
