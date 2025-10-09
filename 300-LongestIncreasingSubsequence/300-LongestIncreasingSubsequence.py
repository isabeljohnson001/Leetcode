# Last updated: 10/8/2025, 9:51:09 PM
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dp(i):
            # base  case
            ans = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    ans = max(ans, dp(j) + 1)
            return ans
        
        return max(dp(i) for i in range(len(nums)))
