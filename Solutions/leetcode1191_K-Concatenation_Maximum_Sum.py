class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        # 题目的复杂度和k本身没有太大的关系，推导k为1和2的情况，在计算k >= 3的情况
        # k >= 3的情况要是不同于k = 1或者2的情况，则此情况下的解一定是横跨了一整个数组.

        if not array:
            return 0

        m = 10 ** 9 + 7

        def maxsum(arr,k):
            refarray = arr * k
            dp = [0] * len(refarray)
            dp[0] = max(0,refarray[0])

            res = max(dp[0],0)

            for i in range(1,len(refarray)):
                dp[i] = max(dp[i], dp[i-1] + refarray[i])
                res = max(dp[i],res)

            return res % m

        if k == 1 or k == 2:
            return maxsum(arr,k) % m

        else:
            total = sum(arr)
            tempmax2 = maxsum(arr,2)
            return max(tempmax2, tempmax2 + (k-2) * total) % m
        
