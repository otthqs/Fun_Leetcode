class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # 利用双指针来进行解题，找到目前的长宽就能算出面积
        # 一开始指针在两侧，在指针移动过程中，牺牲了长度，那么一定要在高处弥补
        # 双指针一次循环

        i, j = 0, len(height) - 1

        res = 0

        while i < j:
            res = max(res,min(height[i],height[j]) * (j-i))
            if height[i] <= height[j]:
                i += 1

            else: j -= 1

        return res
