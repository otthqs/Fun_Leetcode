class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        A = {}
        big = 0
        for num in nums:
            A[num] = A.get(num,0) +1
            if big < A[num]:
                big = A[num]
                res = num

        return res
