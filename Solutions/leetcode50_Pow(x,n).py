class Solution:
    def myPow(self, x: float, n: int) -> float:

    #用分制的思想来解决问题
    #不用记忆化递归的原因是没有多余和重复算的情况
        def helper(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x

            y = helper(x,n//2)
            if n % 2 == 0:
                return y ** 2

            elif n %2 == 1:
                return x * y ** 2


        if n < 0:
            n *= -1
            x = 1/x

        return helper(x,n)
