class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0]
        sell = 0

        for x in prices:
            sell = max(sell, x - buy)
            buy = min(buy,x)

        return sell