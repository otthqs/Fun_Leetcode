class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        # 由于我们可以在board的任意位置为起点进行搜索，必须将所有起点，即整个board遍历一遍，找到一个解就可以返回True
        # 定义另外一个函数dfs来找解，从i,j开始能不能找到匹配word的解

        if not board:
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board,i,j,word):
                    return True

        return False


    def dfs(self,board,i,j,word):
        # 迭代进行找解，每一次找到当前符合的位置，在下个位置传入word[1:]

        # 第一步写 edge case:
        if not word:
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
            return False


        # 当前满足board[i][j] == word[0]
        # 为避免重复搜索，将board[i][j]标记为word中绝不会出现的符号，就不会出现重复搜索
        temp = board[i][j]
        board[i][j] = "#"
        res = self.dfs(board,i+1,j,word[1:]) or self.dfs(board,i-1,j,word[1:]) or self.dfs(board,i,j+1,word[1:]) or self.dfs(board,i,j-1,word[1:])
        board[i][j] = temp

        return res
