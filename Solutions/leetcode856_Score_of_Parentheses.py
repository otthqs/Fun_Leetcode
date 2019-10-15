class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        #用栈的方法来解决问题
        #每次遇到'('将cur的分数入栈，记住下一层的括号，重设cur为0
        #每次遇到')'将cur的分数乘以2，但是最少要为1，并与上一层的分数相加
        #最后返回cur

        cur = 0
        stack = []
        for c in S:
            if c == '(':
                stack.append(cur)
                cur = 0

            elif c == ')':
                cur = max(2 * cur, 1)
                cur += stack.pop()

        return cur
