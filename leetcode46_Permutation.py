class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


        # 每循环一次往空列表里放一个没有的元素
        # 第一次循环后变为 [1],[2],[3]
        # 第二次循环后变为 [1.2],[1.3],[2,1][2,3],[3,1],[3,2]
        # 第三次循环后就把剩下的元素加进去就好了
        # 用list comprehension

        res = [[]]

        for i in range(len(nums)):
            res = [k + [v] for k in res for v in nums if v not in k]

        return res
