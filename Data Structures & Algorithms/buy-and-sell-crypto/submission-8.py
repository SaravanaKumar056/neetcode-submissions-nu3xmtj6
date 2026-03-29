class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        leftMax = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                right = prices[r] - prices[l]
                leftMax = max(leftMax, right)
            else:
                l = r
            r += 1
        return leftMax
