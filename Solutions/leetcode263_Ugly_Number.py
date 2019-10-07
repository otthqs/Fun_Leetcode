class Solution:
    def isUgly(self, num: int) -> bool:
        #ugly number = (2**i) * (3**i) * (5**i)

        if num == 0:
            return False

        for each in [2,3,5]:
            while num % each == 0:
                num /= each


        return num == 1
