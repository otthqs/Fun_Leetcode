class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        # 首先应该考虑正负号的情况，同号为正，异号为负
        negativeflag = (numerator * denominator) < 0
        numerator, denominator = abs(numerator), abs(denominator)

        # 定义重复的小数部分的值
        loopStr = None

        # 定义除的结果
        refList = []

        # 要知道除了多少次，用来定位循环开始的地方
        cnt = 0

        #定义一个字典来记录numerator，如果numerator在字典中出现过，又再次出现，则表明重复开始
        loopDict = {}


        while True:
            refList.append(str(numerator // denominator))
            cnt += 1
            numerator = 10 * (numerator % denominator)

            if numerator == 0:
                break

            #判断是否有重复的值出现，如果有则证明开始循环了
            loc = loopDict.get(numerator)

            if loc:
                loopStr = "".join(refList[loc:cnt])
                break

            loopDict[numerator] = cnt

        res = refList[0]

        if len(refList) > 1:
            res += '.'

        if not loopStr:
            res += ''.join(refList[1:])


        else:
            res += ''.join(refList[1:loc])
            res += '('
            res += loopStr
            res += ')'

        if negativeflag:
            return '-' + res

        else:
            return res
