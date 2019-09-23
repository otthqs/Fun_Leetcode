class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums.insert(0,0)



        i = 1
        while i < len(nums):
            if nums[i] != i and nums[nums[i]] != nums[i]:
                nums[nums[i]],nums[i] = nums[i],nums[nums[i]]

            else:i += 1

        res = []

        for i in range(1,len(nums)):
            if nums[i] != i:
                res.append(i)

        return res
