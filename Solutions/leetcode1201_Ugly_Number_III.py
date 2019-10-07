class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        #猜测一个数字x，用二分法搜索一个数字使得比其小于等于的ugly number有n个即可
        def mcd(a,b):
            if a <= b:
                a,b = b,a
            while b:
                a,b = b, a % b
            return a

        def lcm(a,b):
            return a * b // mcd(a,b)

        low = 1

        high = 2 * 10 **9

        ab = lcm(a,b)
        bc = lcm(b,c)
        ac = lcm(a,c)
        abc = lcm(ab,c)

        while low < high:
            mid = low + (high-low) // 2
            m = mid // a + mid // c + mid // b - mid//ab - mid//ac - mid//bc + mid//abc
            if m < n:
                low = mid + 1
            else:
                high = mid

        return low
