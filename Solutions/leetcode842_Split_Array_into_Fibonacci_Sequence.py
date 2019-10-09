class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        def isValid(first: int, second: int, start: int, num: str) -> bool:
            if start == len(num):
                return True

            sumValue = first + second
            first, second = second, first+second
            return num[start:].startswith(str(sumValue)) and isValid(first, second, start + len(str(sumValue)), num)


        def isFibonacci(num: str):
            if len(num) < 3:
                return [False,0,0]


            for i in range(1,(len(num)//2) + 1):
                if num[0] == '0' and i > 1:
                    return [False,0,0]
                first = int(num[:i])
                j = 1
                while len(num) - i - j >= max(i,j):
                    if num[i] == '0' and j > 1:
                        break
                    second = int(num[i:i+j])

                    if isValid(first, second, i+j, num):
                        return [True,i,j]

                    j += 1

            return [False,0,0]

        res = []
        maxint = 2 ** 31 - 1
        bol, firstNum, secondNum = isFibonacci(S)
        if bol:
            cnt = firstNum + secondNum
            res += [int(S[:firstNum]), int(S[firstNum:cnt])]
            while cnt != len(S):
                tempSum = res[-1] + res[-2]
                if tempSum > maxint:
                    return []
                res.append(tempSum)
                cnt += len(str(tempSum))

        return res
