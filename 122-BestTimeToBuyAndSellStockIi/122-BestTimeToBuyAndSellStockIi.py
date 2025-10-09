# Last updated: 10/8/2025, 9:52:18 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit+=prices[i]-prices[i-1]
        return profit
        