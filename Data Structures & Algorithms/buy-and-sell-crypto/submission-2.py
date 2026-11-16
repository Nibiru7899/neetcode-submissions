class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float("inf")
        maxPro = 0
        for price in prices:
            if price<mini:
                mini = price
            else:
                maxPro = max(maxPro, price-mini)
        return maxPro
            