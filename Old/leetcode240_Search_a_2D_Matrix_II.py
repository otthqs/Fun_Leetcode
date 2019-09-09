class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        # 从一个方向开始搜索，从左下或右上开始搜索即可
        # 如，从右上开始搜搜


        # edge case: matrix为空，返回False
        if not matrix:
            return False

        row = len(matrix)
        col = len(matrix[0])

        i, j = 0, col-1

        while i >= 0 and i <= row-1 and j >= 0 and j<= col -1:
            if matrix[i][j] == target:
                return True

            elif matrix[i][j] > target:
                j -= 1

            else:
                i += 1


        return False
