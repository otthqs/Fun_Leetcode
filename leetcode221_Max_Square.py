class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # 动态规划问题，我们利用一个二维数组表示，到当前位置最大的square的数目.
        # 我们初始化 dp 第一行第一列为matrix的第一行第一列，然后如果matrix[i][j]是1，那么 dp[i][j] 矩形最大的数目是 [i-1][j], [i][j-1], [i-1][j-1]的矩形最小数 加上 1

        if not matrix:
            return 0

        row = len(matrix)
        col = len(matrix[0])

        # 初始化 dp 数组: 建立，进行第一行第一列的初始化

        dp = []

        res = 0

        for i in range(row):
            dp.append([0]*col)

        for i in range(col):
            dp[0][i] = int(matrix[0][i])
            res = max(res,dp[0][i])


        for j in range(row):
            dp[j][0] = int(matrix[j][0])
            res = max(res,dp[j][0])



        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    res = max(res,dp[i][j])

        return res**2
