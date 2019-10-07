class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        #用记忆化递归进行计算（其实就是相当于动态规划）
        #编程为Win(state, num): 表示为当前选了一些列数字之后的某个state，还需要选的数字的和为num才能获胜，那么当前这个人在最优情况下能不能获胜
        # state用bit来表示当前数字有没有选过，一共有maxChoosableInteger那么多个bit

        if sum(range(1,maxChoosableInteger+1)) < desiredTotal:
            return False

        import functools
        @functools.lru_cache(None)
        def dfs(state,num):
            for i in range(1,maxChoosableInteger + 1):
                cur = state >> (i-1) & 1
                if cur == 0:
                    if num - i <= 0:
                        return True

                    if not dfs(state| 1 << (i-1),num - i):
                        return True

            return False

        return dfs(0,desiredTotal)
        
