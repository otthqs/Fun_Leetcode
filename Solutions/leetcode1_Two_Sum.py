class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        refdic = {}

        for i,c in enumerate(nums):
            if target - c in refdic:
                return [refdic[target - c],i]

            else:
                refdic[c] = i
