class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not len(nums):
            return 0

        length = len(nums)

        if length < 2:
            return max(nums)

        dp = []

        dp = [0]*length

        dp[0] = nums[0]
        dp[1] = max(nums[:2])

        for i in range(2,length):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])

        return dp[-1]
