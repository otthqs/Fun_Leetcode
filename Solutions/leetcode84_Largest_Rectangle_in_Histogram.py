class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        #用单调栈来解决问题，首先从左往右找到连续的比heights[i]大的数字，再从右往左找到连续的比heights[i]大的数字，然后遍历一遍找出最大的面积即可
        if not heights:
            return 0

        left = [0] * len(heights)
        right = [0] * len(heights)
        stack = []
        for i in range(len(heights)):
            res = 0
            while stack and heights[i] <= heights[stack[-1][0]]:
                node = stack.pop()
                res += (1+node[1])
                left[i] = res

            stack.append([i,res])

        stack = []
        for i in range(len(heights)-1,-1,-1):
            res = 0
            while stack and heights[i] <= heights[stack[-1][0]]:
                node = stack.pop()
                res += (1+node[1])
                right[i] = res

            stack.append([i,res])

        return max([(left[i] + right[i] + 1) * heights[i] for i in range(len(heights))])
