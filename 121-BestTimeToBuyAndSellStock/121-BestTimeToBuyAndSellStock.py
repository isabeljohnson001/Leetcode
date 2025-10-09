# Last updated: 10/8/2025, 9:52:20 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_profit=float("inf")
        max_profit=0

        for i in range(len(prices)):
            if prices[i]<min_profit:
                min_profit=prices[i]
            elif prices[i]-min_profit>max_profit:
                max_profit=prices[i]-min_profit
        return max_profit

        