class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        ans=0
        curr_zero=0
        for right in range(len(nums)):
            if nums[right]==0:
                curr_zero+=1
            
            while curr_zero>k:
                if nums[left]==0:
                    curr_zero-=1
                left+=1
                #curr_sum-=1
            ans=max(ans,right-left+1)
        return ans
        