class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        # 打算用stack来解决，用栈的形式进行decode和encode，但是memory会溢出，所以用递归的方式解决
#         stack = ['']

#         for c in S:
#             if len(stack[-1]) >= K:
#                 return stack[-1][K-1]

#             if c.isalpha():
#                 stack[-1] += c

#             if c.isdigit():
#                 stack[-1] = stack[-1] * int(c)

#         return stack[-1][K-1]


        # 用递归的方式
        cnt = 0

        for i,c in enumerate(S):
            if c.isalpha():
                cnt += 1

                if cnt == K:
                    return c

            else:
                if cnt * int(c) < K:
                    cnt *= int(c)

                elif K % cnt == 0:
                    return self.decodeAtIndex(S[:i],cnt)

                else:
                    return self.decodeAtIndex(S[:i], K % cnt)
