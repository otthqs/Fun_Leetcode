class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # 利用深度优先搜索进行解题


        res = []

        # 先写edge case
        def helper(nums,path,i,target):
            if target == 0:
                res.append(path)
                return

            if target < 0:
                return

        # 进入循环
        # j从i的位置开始循环，不走回头路
            if target > 0:
                for j in range(i,len(nums)):
                    helper(nums,path+[nums[j]],j,target-nums[j])


        helper(candidates,[],0,target)

        return res
