class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
    # 建立一个搜索函数，把从一个1开始的上下左右含有1的地方都标记：
        def helper(grid,i,j):
        # 先写 edge case
            if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] != "1":
                return
        # 中间过程
            grid[i][j] = "#"

        # 迭代部分 一定注意要四个部分都需要
            helper(grid,i+1,j)
            helper(grid,i-1,j)
            helper(grid,i,j+1)
            helper(grid,i,j-1)


        # 在取迭代的方式进行搜索，遇到一个1，就把它周围的1全部标记为visited，这样循环几次就有几座island
        # grid 开始搜索，进行了几次循环，就有几座岛屿
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    helper(grid,i,j)

        return count
