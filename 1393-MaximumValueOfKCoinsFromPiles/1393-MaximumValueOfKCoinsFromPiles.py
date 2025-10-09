# Last updated: 10/8/2025, 9:49:08 PM
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:


        #you hav 2 steps to do here..either skip or take
        #skip =dp(i+1,remain)
        #take=piles[i][:j]+dp(i+1,remain-j-1)..here j values should not be more thtn pile len or k

        @cache
        def dp(i, remain):

            #base case
            if i==len(piles) or remain==0:
                return 0
            
            ans=dp(i+1,remain)
            curr=0
            for j in range(min(len(piles[i]),remain)):
                curr+=piles[i][j]
                ans=max(ans,curr+dp(i+1,remain-j-1))
            return ans
        return dp(0,k)
        