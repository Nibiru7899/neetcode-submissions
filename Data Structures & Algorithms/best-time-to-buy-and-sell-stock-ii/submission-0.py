class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for p in range (1,len(prices)):
            if prices[p-1] < prices[p]:
                profit += prices[p] - prices[p-1]
        return profit