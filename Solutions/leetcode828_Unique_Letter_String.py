class Solution:
    def uniqueLetterString(self, S: str) -> int:
        #不用去想每一个substring中有多少个数目的unique string，只用去管每一个char in S，能够贡献出多少值在我们的最后的结果中
        #比如###A##A##，其中第一个A可以在index0，1，2，3的左边开始的subtring为起始，即加一个'('表示substring开始，在index4，5，6的左边为终止的substring，即加一个')'为终止的substring，为unique substring，一共能贡献的单位为4*3 = 12
        #用一个refList来记录一个字母上两次出现的位置，在第一次遍历时将最后一次重复出现的字母之前的贡献值都计算好；在第二次遍历时计算没有重复的字母或者重复字母中最后一次重现的字母的贡献值

        refDict = {c:[-1,-1] for c in S}
        res = 0
        for i,c in enumerate(S):
            k,j = refDict[c]
            res += (j-k) * (i-j)
            refDict[c] = [j,i]

        visited = set()
        for c in S:
            if c not in visited:
                k,j = refDict[c]
                res += (j-k) * (len(S) - j)
                visited.add(c)

        return res % (10**9+7)

            
