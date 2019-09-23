class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        #判断边界情况是否为没有雨的情况
        if len(height) == 0 or len(height) ==1 or len(height) ==2:
            return 0
        total = 0

        #找到最高的一个壁垒，那么在壁垒左边和右边，能不能储存雨，就看左边最高的壁垒和当前壁垒的关系
        high = height.index(max(height))
        lefmax = height[0]
        rhtmax = height[len(height)-1]

        for i in range(0,high):
            if lefmax > height[i]:
                total += (lefmax-height[i])
            else:
                lefmax = height[i]

        for i in range(len(height)-1,high,-1):
            if rhtmax > height[i]:
                total += (rhtmax-height[i])
            else:
                rhtmax = height[i]
        return total
