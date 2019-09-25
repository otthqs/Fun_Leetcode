class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()
        start = 0
        sign = 1

        if not s:
            return 0

        if s[0] == '-':
            sign = -1
            start = 1
        elif s[0] == '+':
            start = 1
        elif not s[0].isdigit():
            return 0

        result = 0
        for char in s[start:]:
            if not char.isdigit():
                break
            result = result * 10 + int(char)

        result *= sign

        MaxValue = 2**31 - 1
        MinValue = -2**31
        if result < MinValue:
            return MinValue
        if result > MaxValue:
            return MaxValue
        return result
