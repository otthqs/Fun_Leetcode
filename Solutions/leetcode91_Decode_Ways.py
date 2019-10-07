class Solution:
    def numDecodings(self, s: str) -> int:
        # 应用dp来解决问题，dp[i]表示前i个元素的decode的方式
        # 如果第i个元素看成单独的一种，则为dp[i-1],如果i和i-1元素是合法的一种解读的方式则看成dp[i-2]解读方式

        if len(s) <= 0 or s[0] == '0':
            return 0

        if len(s) == 1 and s[0] != '0':
            return 1


        dp =[1] + [0] * (len(s) - 1)

        if s[1] == '0':
            if '01'<= s[:2] <= '26':
                dp[1] = 1
        else:
            dp[1] = 1

            if  '01'<= s[:2] <= '26':
                dp[1] += 1


        for i in range(2,len(s)):
            if s[i] == '0':
                if '01' <= s[i-1:i+1] <= '26':
                    dp[i] += dp[i-2]

            else:
                dp[i] += dp[i-1]

                if '11' <= s[i-1:i+1] <= '26':
                    dp[i] += dp[i-2]

        return dp[-1]
