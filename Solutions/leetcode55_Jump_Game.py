class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # DP问题，更新一个从当前位置能到的最远位置，如果最远位置比数组的长度长，那么就可以跳到结尾

        if not nums or len(nums)==1:
            return True

        res = nums[0]

        i = 0

        while i <= res:
            if res >= len(nums)-1:
                return True

            res = max(res,i+nums[i])

            i += 1

        return False
