class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minProfit = prices[0]

        for sell in prices:
            minProfit = min(minProfit, sell)
            maxProfit = max(maxProfit, sell - minProfit)
        return maxProfit