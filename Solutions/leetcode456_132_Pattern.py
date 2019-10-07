class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # 首先我们需要预处理一下数据，找到i之前最小的数字

        # 从后往前用单调栈的形式找出次小的，维护一个递减的序列: 9 8 7 6 5
        # 从后往前的过程中遇到上扬的情况  9 8 7 6 5 7， 则考虑7作为中间的pattern‘3’，利用退栈的原理找出一个最接近7但是比7小的数字作为pattern‘2’，比较目前是否能形成132的pattern的形式。如果不能则继续维护一个递减的序列
        # 退栈的元素不需要保留，因为他们被退栈的判断时，是没有当时的次高高的，所以不用考虑

        if len(nums) < 3:
            return False

        minNum = nums[0]
        refList = [minNum]
        for i in range(1,len(nums)):
            minNum = min(minNum, nums[i])
            refList.append(minNum)

        refStack = []
        for i in range(len(nums)-1,-1,-1):
            if refStack and nums[i] > refStack[-1]:
                middle = nums[i]
                while refStack and nums[i] > refStack[-1]:
                    right = refStack.pop(-1)

                if middle > refList[i] and right > refList[i]:
                    return True

            refStack.append(nums[i])

        return False
                    
