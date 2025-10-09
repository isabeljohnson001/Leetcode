# Last updated: 10/8/2025, 9:52:03 PM
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        @cache
        # buy,sell,skip
        #buy ---that means we are not holding any stock =-price[i]+dp(i (nextday)+1),True,remain)
        #sell ---that means we are holding a stock =price[i]+dp(i (nextday)+1),False,remain-1)
        #skip ---that means we can skip from buy or sell =dp(i (nextday)+1),holding,remain)

        def dp(i, holding, remain):

            #base case wen we reach at the end of the array or we run out of k
            if i==len(prices) or remain<=0:
                return 0

            ans=dp(i+1, holding, remain)

            if holding:
                ans=max(ans,prices[i]+dp(i+1,False,remain-1))
            else:
                ans=max(ans,-prices[i]+dp(i+1,True,remain))
            
            return ans
        return dp(0,False,k)
        