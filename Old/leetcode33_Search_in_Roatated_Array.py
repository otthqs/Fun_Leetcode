class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # 时间复杂度是 O(nlogn) 只能用二分搜索来做，二分搜索关键处在于判断目标所在的区间

        low, high = 0, len(nums)-1

        while low <= high:
            mid = (low+high)//2

            if nums[mid] == target:
                return mid

        # 只有一个轴是转折点，如果 nums[low] < nums[mid]， 转折点在mid之后， 从low到mid时递增序列
            if nums[low] <= nums[mid]:
                if nums[mid] > target >= nums[low]:
                    high = mid-1

                else:
                    low = mid+1

        # 转折点在mid之前， 从mid到high似乎递增序列,在次序列判断target在不在
            else:
                if nums[high] >= target > nums[mid]:
                    low = mid+1

                else:
                    high = mid-1

        else:
            return -1
