class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        # scan through the list, if encounter a drop: previous value larger than next one
        # update min, max, so after scan, we know the min, and max of the most mis-placed target
        # then we do final scan to get the index where the target max and min should placed

        # scan to get target min and max
        minVal, maxVal = float("inf"), float("-inf")
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]: # encounter a drop, update min and max
                minVal = min(minVal, nums[i])
                maxVal = max(maxVal, nums[i-1])

        # if no min max value updated, a list is sorted
        # print(minVal, maxVal)
        if minVal == float("inf"):
            return 0

        # final scan to get the target index
        start, end = 0, len(nums)-1

        while nums[start] <= minVal:
            start += 1

        while nums[end] >= maxVal:
            end -= 1

        return end - start + 1
