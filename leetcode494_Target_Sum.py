class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        # 是一个动态规划问题，先写edge case 如果nums为空，那么唯有能组成0这个和
        if not nums:
            if S==0:
                return 1
            else:
                return 0

        # 如果nums不为空，则可以进行动态规划字典的初始化
        # 初始化话的状态为，只用第一个数，能组成的和作为key，组成这个和的种类数为value
        dic = {nums[0]:1, -nums[0]:1} if nums[0]!=0 else{0:2}

        # 接下来开始动态规范，每一次循环就是在上一次基础上看，能组成的和为key，次数为value
        for i in range(1,len(nums)):
        # 创建一个空子典作为暂时变量来储存新生成的字典
            temp = {}
            for k in dic:
                temp[k+nums[i]] = temp.get(k+nums[i],0) + dic[k]
                temp[k-nums[i]] = temp.get(k-nums[i],0) + dic[k]
            dic = temp

        return dic.get(S,0)
