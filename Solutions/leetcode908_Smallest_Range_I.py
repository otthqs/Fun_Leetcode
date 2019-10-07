class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        # 只用比较最小的和最大的两个数之间的range就可以了

        if len(A) <= 1:
            return 0

        small, big = A[0], A[0]

        for c in A:
            small = min(small,c)
            big = max(big, c)

        if small + abs(K) >= big - abs(K):
            return 0

        else: return big - 2 * abs(K) - small
