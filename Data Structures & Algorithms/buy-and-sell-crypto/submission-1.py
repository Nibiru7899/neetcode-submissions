class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minimum = float("inf")
        for price in prices:
            if price<minimum:
                minimum = price
            maxProfit = max(maxProfit, price-minimum)
        return maxProfit