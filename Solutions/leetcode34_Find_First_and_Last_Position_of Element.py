class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 为满足时间复杂度的要求，要用二分搜索搜寻这个target的左端点和右端点，搜索停止条件比起一般的二分搜索产生变化

        def leftpoint(nums,target):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high)//2
                if nums[mid] == target:
                    # 搜索停止条件：当为最左端，或者在左边一个元素的值不为target
                    if mid == 0 or nums[mid-1] != target:
                        return mid

                    else: high = mid - 1

                elif nums[mid] > target:
                    high = mid - 1

                else:
                    low = mid + 1

            else: return -1

        def rightpoint(nums,target):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high)//2
                if nums[mid] == target:
                    # 搜索停止条件：当为最右端，或者在又边一个元素的值不为target
                    if mid == len(nums)-1 or nums[mid+1] != target:
                        return mid

                    else: low = mid + 1

                elif nums[mid] > target:
                    high = mid - 1

                else:
                    low = mid + 1

            else: return -1

        left = leftpoint(nums,target)
        right = rightpoint(nums,target)

        return [left,right]
