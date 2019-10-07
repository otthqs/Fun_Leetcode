class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        #将list进行排序，目的是缩小差距，则需要找一个分解点，在分解点右边的全部-K，分界点左边的全部加K
        # 1  2  || 3   4   5   6  7  8  9
        # 最大值出现在分界点左边的第一个数加K，最后一个数减K
        # 最小值出现在，第一个数加K，分界点右边第一个数减K

        if len(A) <= 1:
            return 0

        A.sort()
        res = A[-1] - A[0]
        for i in range(1,len(A)):
            big = max(A[i-1]+ abs(K), A[-1] - abs(K))
            print(big)
            small = min(A[i] - abs(K), A[0] + abs(K))
            print(small)
            res = min(res,big - small)

        return res
