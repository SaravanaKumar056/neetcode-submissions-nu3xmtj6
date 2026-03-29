class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrices = prices[0]

        for sell in prices:
            minPrices = min(minPrices, sell)
            maxProfit = max(maxProfit, sell - minPrices)
        return maxProfit