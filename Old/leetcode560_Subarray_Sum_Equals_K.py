class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # 要求连续subarray的和是一个target
        # 我们维护一个presum的字典，表示前i-1个数字组成的所有subarray能取到的“和” 以及这个和出现的次数
        #那么前i个和的sum为res，那么如果res-k在presum的字典中，那么就存在一个以第i个元素结尾的subarray和为k

        #初始化 presum = {0:1}，这样就包含了，整个sum等于k的情况

        if not nums:
            return 0

        presum = {}
        presum[0] = 1

        count = 0
        res = 0

        for i in range(len(nums)):
            #计算到第i个元素的和
            res += nums[i]

            #如果 res-k存在，那么subarray存在：
            if res-k in presum:
                count += presum[res-k]

            #更新presum字典
            presum[res] = presum.get(res,0) + 1

        return count
