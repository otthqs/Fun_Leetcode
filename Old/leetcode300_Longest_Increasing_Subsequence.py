class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 动态规划问题，维护一个一维数组 dp
        # dp [i] 表示到第i个元素为止，最长的increase subsequence是多少
        # 下一个dp[i]，就循环看当前位置的 nums[i]，是否比之前的nums[i]大
        # 更大的话 dp[i] 就是当前dp[i] 和 dp[j] + 1 中取更大的那个值

         # 处理边缘的edge case
        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        dp = [1] * len(nums)

        res = 0

        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
                if res <= dp[i]:
                    res = dp[i]

        return res
