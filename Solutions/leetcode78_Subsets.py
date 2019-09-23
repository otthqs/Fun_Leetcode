class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # 由前n个元素构成的子集是由n-1个元素构成的子集加上第n个元素和前n-1个子集构成的集合

        # 由0个元素构成的子集
        res = [[]]

        # 进入循环，算多一个个元素后构成的集合

        for num in nums:
            res_new = [k + [num] for k in res]
            res += res_new

        return res
