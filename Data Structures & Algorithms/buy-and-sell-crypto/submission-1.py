class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currBuy = prices[0]
        maxProf = 0
        for num in prices:
            currProf = num - currBuy
            if currProf < 0:
                currBuy = num
            else:
                maxProf = max(maxProf, currProf)
        return maxProf