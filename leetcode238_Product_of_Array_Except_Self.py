class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 采用两次循环来进行解决
        # 初始化结果为 [1] * len(nums)
        # 第一次循环从前往后，将所处位置之前的所有成绩乘到数字上
        # 第二次循环从后往前，强所处位置之后的所有成绩乘到数字上


        res = [1] * len(nums)

        temp = nums[0]

        for i in range(1,len(nums)):
            res[i] *= temp
            temp *= nums[i]

        temp = nums[-1]

        for i in range(len(nums)-2,-1,-1):
            res[i] *= temp
            temp *= nums[i]

        return res
