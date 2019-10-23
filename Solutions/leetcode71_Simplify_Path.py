class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')

        for item in path:

            if item == '.' or item == '':
                continue
            elif item == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(item)

        res = '/'.join(stack)
        res = '/' + res
        return res
