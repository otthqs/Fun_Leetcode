class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 因为有负数的存在，最大的subarray只会出现在截止上一个数最大的product，和截止上一个数最小的product和目前数目的乘积之间
        # 对数组进行初始化
        big = [nums[0]] + [float("-inf")]*(len(nums)-1)
        small = [nums[0]] + [float("inf")]*(len(nums)-1)

        res = nums[0]

        for i in range(1,len(nums)):
            big[i] = max(big[i-1]*nums[i],small[i-1]*nums[i],nums[i])
            small[i] = min(big[i-1]*nums[i],small[i-1]*nums[i],nums[i])

            if res < big[i]:
                res = big[i]

        return res
            
