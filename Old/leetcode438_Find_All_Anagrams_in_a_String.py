class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #不用管字母的顺序，26个字母对应成一个字典或者列表，将p用这个列表表示，每次判断字典是否相等即可

        reflst = [0] * 26
        dp = [0] * 26

        res = []

        for unit in p:
            reflst[ord(unit) - ord('a')] += 1

        for i,c in enumerate(s):

            dp[ord(c) - ord('a')] += 1

            if i < len(p)-1:
                continue

            if dp == reflst:
                res.append(i + 1 - len(p))

            dp[ord(s[i+1-len(p)]) - ord('a')] -= 1


        return res
