class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        # 这是一个动态规划问题，维护一个一维数组，dp[i]表示s中从头到第i个元素（包括第i个）能不能被wordDict组合而成

        # set用hash算法，搜索速度最快
        wordDict = set(wordDict)

        # 对 dp 进行初始化，设置为全为False
        dp = [False]*len(s)




        for i in range(len(s)):
            if s[:i+1] in wordDict:
                dp[i] = True
                continue

            for j in range(i):
                if dp[j] == True and s[j+1:i+1] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]
