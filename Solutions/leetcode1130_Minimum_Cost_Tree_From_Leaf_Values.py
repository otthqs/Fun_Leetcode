用区间dp来做，简化为记忆化递归来写
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def dp(i,j):
            if j - i > 0:
                return min(dp(i,k-1) + dp(k,j) + max(arr[i:k])*max(arr[k:j+1]) for k in range(i+1,j+1))
            return 0

        return dp(0,len(arr)-1)


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        #可以将原问题看成合并数字的问题，要是合并6，2，那么cost为12，留下的数字为6；要是合并2，4则cost为8，留下的数字为4，留下的数字为大的数字
        #原问题可以转换为求最小的cost的问题，知道合并到最后的数字剩余1个
        #要合并一个数字A[i]的最小的cost，我们需要求为A[i]左边第一个比A[i]大的数字left和A[i]右边第一个比A[i]大的数字right，那么最小的cost = min(left,right) * A[i]
        #运用单调栈来解决

        res = 0
        stack = [float('inf')]

        for c in arr:
            while len(stack) > 1 and c >= stack[-1]:
                node = stack.pop()
                res += node * min(c, stack[-1])

            stack.append(c)

        while len(stack) > 2:
            mid = stack.pop()
            res += mid * stack[-1]

        return res
