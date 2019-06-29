class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        #  关于一个nums的next permutation其实是：
        # 从后往前找到一个数字非递增，把这个数字和它之后的第一个大于它的数字互换，在将这个数字后面的数字反序排列
        #  列如 1 2 7 4 3 1， 我们先找到数字2，因为非递增，再将数字2和数字3互换位置得到：
        # 1 3 7 4 2 1，在将3后面的数字反徐排列得到：
        # 1 3 1 2 4 7

        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                for j in range(len(nums)-1,i-1,-1):
                    if nums[j] > nums[i-1]:
                        nums[i-1],nums[j] = nums[j], nums[i-1]
                        nums[i:] = sorted(nums[i:])
                        return






        else: nums.reverse()

        return
