class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dp(i):

            ans=1 #base case

            for j in range(i):
                if nums[i]>nums[j]:
                    ans=max(ans,dp(j)+1)
            return ans
        
        return max(dp(i) for i in range(0,len(nums)))
            
        