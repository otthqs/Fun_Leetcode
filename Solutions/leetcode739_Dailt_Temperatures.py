class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        # 用单调栈来求解，所有元素进栈，出栈一次
        res = [0] * len(T)
        stack = []

        # 遍历元素
        for i in range(len(T)):

            #判断当前stack中的元素是否出栈，即判断当前是否找到了一个更高的气温
            while stack and T[stack[-1]] < T[i]:
                ind = stack.pop()
                res[ind] = i - ind

            stack.append(i)


        return res
