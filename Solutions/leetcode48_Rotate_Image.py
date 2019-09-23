class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        # 先进行行列交换进行转置，在将每一行进行倒叙即可

        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]


        for i in range(len(matrix)):
            matrix[i].reverse()
        
