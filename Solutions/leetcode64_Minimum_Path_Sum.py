class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 动态规划问题，到达一个点最短路径为达到此点的左边最短路径，上边最短路径加次点的值
        # 初始化二位数组的第一行第一列的累加值

        # 注意dp矩阵上任意一点不能代表到这点的最短路径，dp[-1][-1]能代表到从左上到右下距离的原因是：从左上到右下的最短路径一定按照一个规则：“每一步只能朝右或朝下”，满足这个规则的dp上的点，才能表示到此点的最短距离


        if not grid:
            return 0

        row,col = len(grid),len(grid[0])

        dp = []

        for i in range(row):
            dp.append([0]*col)

        dp[0][0] = grid[0][0]

        for i in range(1,row):
            dp[i][0] = dp[i-1][0]+grid[i][0]

        for i in range(1,col):
            dp[0][i] = dp[0][i-1]+grid[0][i]


        for i in range(1,row):
            for j in range(1,col):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]

        return dp[-1][-1]
