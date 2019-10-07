class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #用贪婪算法进行计算，在一个stack中，没遇到一个降序就将前一个数字去除掉
        #贪婪算法有效的原因是，在去除K个digit后，数字的长度一样，如果在靠近左边的数字没有变小（没有使用贪婪算法的话），那整体数字一定不是最小的

        if len(num) == k:
            return '0'

        nums = list(map(int,num))
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] < stack[-1] and k > 0:
                stack.pop(-1)
                k -= 1

            stack.append(nums[i])

        while k > 0:
            stack.pop(-1)
            k -= 1

        return str(int(''.join(map(str,stack))))
