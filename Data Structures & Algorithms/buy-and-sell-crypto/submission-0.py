class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = prices[0]

        for price in prices:
            if price < low:
                low = price
            elif profit < price - low:
                profit = price - low
                
        return profit