class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 这道题是求一个数组nums中，是不是有几个数加起来等于和的一半
        # 利用动态规划维护一个一维数组，长度为从0到数组的sum，初始化为0，把每一个数字从后往前遍历，能形成和就把dp数组标记为1

        res_sum = sum(nums)
        if res_sum % 2 != 0:
            return False

        target = res_sum // 2

        dp = [1] + [0]*res_sum


        # 从后往前更新是防止同样一个数字被加两次，列入一个数字是13，那么第一次循环的时候，因为
        # dp[0] == 1，那么 dp[13] = 1, 紧接着 dp[26] = 1
        # 因此我们要从后往前
        for unit in nums:
            for i in range(res_sum,0,-1):
                if i - unit >=0 and dp[i-unit] == 1:
                    dp[i] = 1

            if dp[target] == 1:
                return True

        return False
