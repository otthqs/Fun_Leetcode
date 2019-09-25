class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        #利用桶排序的方法来进行解题。
        #首先用sliding-window的方法来确定k的值的大小
        #将每个数字放入桶内，来看是否在同一桶内或者相临桶内即可

        if t < 0 or k < 0:
            return False

        bucketDict = {}

        #为了防止t为0的情况
        size = t + 1

        for i in range(len(nums)):
            ind = nums[i] // size

            if ind in bucketDict:
                return True

            if (ind + 1) in bucketDict and bucketDict[ind + 1] - nums[i] <= t:
                return True

            if (ind - 1) in bucketDict and nums[i] - bucketDict[ind - 1] <= t:
                return True

            bucketDict[ind] = nums[i]


            if i >= k:
                del bucketDict[nums[i-k] // size]


        return False

        
