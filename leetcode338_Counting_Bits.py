class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        # 采用动态规划进行解决，利用已经的结果来进行迭代

        if num == 0:
            return [0]

        if num == 1:
            return [0,1]



        dp = [0,1] + [0]*(num-1)

        exp_now = 2
        exp_before = 1

        for i in range(2,len(dp)):
            if i == exp_now:
                dp[i] = 1
                exp_before = exp_now
                exp_now *= 2

            elif i < exp_now:
                dp[i] = dp[exp_before] + dp[i-exp_before]

        return dp
