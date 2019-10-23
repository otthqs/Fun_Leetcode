class Solution:
    def findNthDigit(self, n: int) -> int:
        #先找出目前n是在哪一层，0-9， 10 - 99， 100 - 999
        #在找出是在哪一个具体的数字的第几位数，返回出来第几位数即可
        layer = 1
        while n > 0:
            layerNum = 9 * (10 ** (layer-1))
            n -= layerNum * layer
            layer += 1

        layer -= 1
        n += layerNum * layer

        mod = n % layer
        if mod == 0:
            return int(str(10 ** (layer-1) + n // layer - 1)[-1])

        else:
            return int((str(10 ** (layer-1) + n // layer)[mod-1]))
        
