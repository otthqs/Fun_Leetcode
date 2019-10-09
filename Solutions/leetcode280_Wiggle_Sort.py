class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #用O(1)extra space来解决，先将array排序，然后将一个一个pair换顺即可

        nums.sort()
        for i in range(1,len(nums)-1,2):
            nums[i],nums[i+1] = nums[i+1],nums[i]
