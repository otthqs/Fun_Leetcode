class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 返回组成一个数字的最小的 square 的数字的数目,利用动态规划问题来求解
        # 维护一个一维数组，表示从0开始到n，每一个数，最少需要多少 square来构成：

        if n == 0 or n == 1:
            return n

        dp = [0] + [float("inf")]* n

        for i in range(1,len(dp)):
             # 对第二层循环的时候，一定要注意，在 (i**0.5)后面 +1，确保循环能顺利进行
            for j in range(int(i**0.5)+1):
                if i - j**2 >=0:
                    dp[i] = min(dp[i],dp[i-j**2]+1)
                else:
                    break

        return dp[-1]
