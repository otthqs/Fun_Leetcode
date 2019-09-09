class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 动态规划问题，dp[i]为换取数目为i的钱最少的硬币数，如果换取不了，则定义为inf
        # 初始条件为换取 0 只需要 0 个硬币即可

        coins.sort()

        dp = [0] + [float("inf")]*amount
        for i in range(1,len(dp)):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i],dp[i-coin]+1)
                else: break

        if dp[-1] == float("inf"):
            return -1

        return dp[-1]
