class Solution:
    def nextGreaterElement(self, n: int) -> int:
        #和next permutation一样，找到下一个更高一点的数字
        #将n变成一个个数字反序装入list中，如n为122，则nums = [2,2,1]

        nums = list(map(int,str(n)[::-1]))
        stack = [0]
        for i in range(1,len(nums)):
            if nums[i]>= nums[i-1]:
                stack.append(i)

            else:
                break
        else:
            return -1

        while stack and nums[stack[-1]] > nums[i]:
                    node = stack.pop()

        nums[node],nums[i] = nums[i], nums[node]

        nums[:i] = sorted(nums[:i], reverse = True)

        n = int(''.join(list(map(str,nums[::-1]))))

        if n > (1<<31):
            return -1

        else:
            return n

            
