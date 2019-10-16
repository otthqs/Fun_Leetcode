class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        #首先注意题目是subsequence，不是subarray，所以不用考虑原来的顺序。
        #如果对A进行排序，对于A[i]，有i个数字比A[i]小，则A作为最大的数字的subsequence一共有2^i个。同时比A[i]大的数字有len(A) - i - 1个，所以以A作为最小数字的subsequence有2^(len(A) - i - 1)个
        #其中只有只含A[i]的subsequence被重复计算利用，但是重复的这个subsequence不影响计算结果
        #注意在计算 2**i的时候用 1 << i来代替，大大降低计算所需要的时间

        A.sort()
        Length = len(A)
        res = 0

        for i,c in enumerate(A):
            res += ((1 << i) - (1 << (Length - i - 1))) * c

        return res % (10 ** 9 + 7)
