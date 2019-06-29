class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        # 用stack的数据结构来进行
        # 初始化为 stack = [""]
        # 遇到字母就 stack[-1] += 字母
        # 如果遇到数字就看stack[-1]是不是数字，是的话就加在一起不是的话就添加这个元素入栈
        # 遇到 “[”,就又添加一个“”元素入栈，遇到“]” 就开始出栈

        stack = [""]

        for unit in s:
            if unit.isalpha():
                stack[-1] += unit

            elif unit.isdigit():
                if stack[-1].isdigit():
                    stack[-1] += unit

                else:
                    stack.append(unit)

            elif unit == "[":
                stack.append("")

            elif unit == "]":
                tail = stack.pop()
                num = int(stack.pop())
                stack[-1] += num*tail


        return stack[0]
