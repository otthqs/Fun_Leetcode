class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #用区间递归的办法来做，dp[i][j]表示从下标为i到j的能得到的最大值
        #转移方程为dp[i][j] = dp[i][k] + dp[k+1][j+1] + nums[k] * nums[i-1] * nums[j+1]
        #写循环时候需要从长度为1的区间开始写到长度为len(nums)的区间
        #为了计算方便，将nums的头尾插入补丁数字1

        Length = len(nums)
        nums.insert(0,1)
        nums.append(1)

        dp = []
        for i in range(len(nums)):
            dp.append([0] * len(nums))

        for l in range(1,Length + 1):
            for i in range(1,Length-l+2):
                j = i + l - 1
                for k in range(i,j+1):
                    dp[i][j] = max(dp[i][j], dp[i][k-1] + dp[k+1][j] + nums[k] * nums[i-1] * nums[j+1])

        return dp[1][Length]


#记忆化递归的写法如下
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        Length = len(nums)
        nums.append(1)
        nums.insert(0,1)

        from functools import lru_cache
        @lru_cache(None)
        def dp(i,j):
            if j - i >= 0:
                return max(dp(i,k-1) + dp(k+1,j) + nums[k] * nums[i-1] * nums[j+1] for k in range(i,j+1))

            return 0

        return dp(1,Length)
