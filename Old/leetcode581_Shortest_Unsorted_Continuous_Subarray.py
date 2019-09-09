class Solution:
    def findUnsortedSubarray(self, nums: 'List[int]') -> 'int':

        # 注意到我们可以将列表排序，从头和尾比对排序后的列表和排序前的列表，找到序列不同的地方即可

        nums_temp = sorted(nums)

        i,j = 0, len(nums)-1

        while i < len(nums):
            if nums[i] == nums_temp[i]:
                i += 1

            else:
                break

        else:return 0

        while j >= 0:
            if nums[j] == nums_temp[j]:
                j -= 1

            else:
                break


        return j - i + 1
