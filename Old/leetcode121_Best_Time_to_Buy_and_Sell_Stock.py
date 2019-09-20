class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # reduced dimension program.
        if not prices:
            return 0

        low = prices[0]
        gain = 0

        for i in range(1,len(prices)):
            low = min(low,prices[i])
            gain = max(gain,prices[i]-low)

        return gain
