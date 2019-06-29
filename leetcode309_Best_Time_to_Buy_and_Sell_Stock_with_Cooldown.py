class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # 用动态规划来做这道题，先分析我们一共拥有的状态：
        # 一共有三种状态，rest状态：什么都不做，hold状态：持有股票状态，sold状态：卖股票的状态
        # 更新数组 rest，hold，sold，rest[i]，表示第i天为rest状态的话的最大收益
        # 那最后一天的收益最大值就是这三个一维数组的最大值

        # 分析转移状态： rest状态可以转移到rest状态也可以转移到hold状态
        # hold状态可以转移到hold状态，也可以到sold状态
        # sold状态只能转移到rest状态

        # 初始化状态，rest[0] = 0, hold[0] = float("-inf"), sold[0] = float("-inf")

#         rest = [0] + [float("-inf")]*len(prices)
#         hold = [float("-inf")] + [float("-inf")]*len(prices)
#         sold = [0] + [float("-inf")]*len(prices)

#         for i in range(1,1+len(prices)):
#             rest[i] = max(rest[i-1],sold[i-1])
#             hold[i] = max(rest[i-1]-prices[i-1],hold[i-1])
#             sold[i] = hold[i-1] + prices[i-1]

#         return max(rest[-1],hold[-1],sold[-1])


          #由于在整个过程中，只用到了三个一维数组的前一位，因此可以进行降维处理，只需注意更新的时候需要三个变量同时更新即可
        rest, hold, sold = 0, float("-inf"), float("-inf")

        for i in range(len(prices)):
            sold,hold,rest = hold+prices[i], max(rest-prices[i],hold), max(rest,sold)

        return max(sold,hold,rest)
