class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # 用dp的做法来做，用dp[i][k]表示用i个dice扔出k的个数，初始化为dp[0][0] = 1

        if d * f == target:
            return 1

        if d * f < target:
            return 0

        dp = []
        for i in range(d+1):
            dp.append([0] * (d*f + 1))

        dp[0][0] = 1

        m = 10 **9 + 7

        for i in range(1,d+1):
            for k in range(1,f+1):
                for j in range(i-1+k, min(target+1, i*f+1)):
                    dp[i][j] = (dp[i][j] + dp[i-1][j-k]) % m

        print(dp)
        return dp[d][target]
