class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        #判断一个数是否能构成additive number，只用确定这个数字的前两位即可
        #i表示第一个数字的长度，j表示第二个数字的长度，在来确定由这两个数字能否构成additive number

        def isValid(first: int, second: int, start: int, num: str) -> bool:
            if start == len(num):
                return True

            sumValue = first + second
            first, second = second, first+second
            return num[start:].startswith(str(sumValue)) and isValid(first, second, start + len(str(sumValue)), num)



        if len(num) < 3:
            return False


        for i in range(1,(len(num)//2) + 1):
            if num[0] == '0' and i > 1:
                return False
            first = int(num[:i])
            j = 1
            while len(num) - i - j >= max(i,j):
                if num[i] == '0' and j > 1:
                    break
                second = int(num[i:i+j])

                if isValid(first, second, i+j, num):
                    return True

                j += 1

        return False
                
