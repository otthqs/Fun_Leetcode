class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        #我们打算找A[i]作为subarray的数字中最小的数字的array的个数，所以最后的结果是A[i] * f(i)，f(i)为以A[i]作为最小值的array的个数
        #为了寻找f(i)，我们需要先找left[i]，在A[i]之前，比A[i]大的连续的数字的个数，也要寻找right[i]，表示在A[i]之后比A[i]大的连续的数字的个数，自己f(i) = (left[i] + 1) * (right[i] + 1)
        #最后的答案是res = sum(A[i] * f(i))

        left = [0] * len(A)
        right = [0] * len(A)

        stack = []
        for i in range(len(A)):
            res = 1
            while stack and A[i] < A[stack[-1][0]]:
                node = stack.pop()
                res += node[1]
            left[i] = res

            stack.append([i,res])

        stack = []
        for i in range(len(A)-1,-1,-1):
            res = 1
            while stack and A[i] <= A[stack[-1][0]]:
                node = stack.pop()
                res += node[1]
            right[i] = res

            stack.append([i,res])

        print(left)
        print(right)

        return sum([(l) * (r) * c for l,r,c in zip(left,right,A)]) % (10 ** 9 + 7)


            
