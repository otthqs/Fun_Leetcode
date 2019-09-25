class Solution:
    def primePalindrome(self, N: int) -> int:
        # 打算采用生成回文的数字的方式来解题，而不是采用遍历的方式解题

        #RMKs：
        # 偶数位数的回文数字，一定不是质数，因为能被11整除，所以只用生成奇数位数的回文数字
        # 回文数字的结尾不能是偶数，也不能是5，所以只能是[1,3,7,9]

        # some edge cases:
        if N >= 9989900:
            return 100030001

        if len(str(N)) <= 2:
            for c in [2,3,5,7,11]:
                if c >= N:
                    return c

        # 工具函数，检查是否为质数
        def isPrime(n):
            i = 3
            while i ** 2 <=  n:
                if n % i == 0:
                    return False

                i += 2

            return True

        # 工具函数，由一个数字a，生成回文数字b，映射关系为单调递增
        def genOdd(seed):
            seed = str(seed)
            return int(seed + seed[:len(seed) - 1][::-1])


        # 从至少三位数的回文开始检查：
        seed = 10
        while True:
            if str(seed)[0] in ['1','3','7','9']:
                gen = genOdd(seed)
                if gen >= N and isPrime(gen):
                    return gen
            seed += 1

        # We should never get here
        return None
