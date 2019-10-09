# class Solution:
# 	def wiggleSort(self, nums: List[int]) -> None:
# 		"""
# 		Do not return anything, modify nums in-place instead.
# 		"""
#
#         #用O(1)space来解决问题，先将序列倒排，然后将一个个大的数字插入小的数字之间
#
# 		nums.sort(reverse = True)
# 		n = len(nums) // 2
# 		pos = len(nums) // 2
# 		while n > 0:
# 			nums.insert(pos, nums.pop(0))
# 			n -= 1
# 			pos += 1


class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
