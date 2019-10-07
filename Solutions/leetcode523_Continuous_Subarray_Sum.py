class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 此题思路和sum array equal to K一样，但是要注意判断 size at least 2的情况
        # 采用取余数的思想来做，所以要注意目标k == 0的情况

        if len(nums) <= 1:
            return False

        for i in range(len(nums)-1):
            if nums[i] == 0 and nums[i+1] == 0:
                return True

        if k == 0:
            return False

        presum = 0
        nowsum = nums[0]
        refdic = {nowsum % k : 1}
        for i in range(1,len(nums)):
            presum = nowsum
            nowsum += nums[i]

            mod = nowsum % k

            if mod == 0:
                return True

            if refdic.get(mod,0) >= 2:
                return True
            elif refdic.get(mod,0) >= 1 and presum % k != mod:
                return True

            refdic[mod] = refdic.get(mod,0) + 1

        return False

        
