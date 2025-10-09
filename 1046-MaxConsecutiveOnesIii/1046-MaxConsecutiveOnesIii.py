# Last updated: 10/8/2025, 9:49:31 PM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left=curr=ans=0
        for right in range(len(nums)):
            if nums[right]==0:
                curr+=1
            while curr>k:
                if nums[left]==0:
                    curr-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans
    
    
  