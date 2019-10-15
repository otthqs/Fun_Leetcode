class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        #用单调栈来解决，将输入变成两倍长度即可

        nums = nums * 2
        res = [-1] * len(nums)
        stack = []

        for i,c in enumerate(nums):
            while stack and c > nums[stack[-1]]:
                node = stack.pop()
                res[node] = c
            stack.append(i)

        return res[:len(res)//2]
