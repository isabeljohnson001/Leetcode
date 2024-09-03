import sys
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left=0
        curr_sum=0
        ans=float('inf')
        for right in range(len(nums)):
            #creting the slidign window
            if curr_sum<target:
                curr_sum+=nums[right]
                
            while curr_sum>=target:
                ans=min(ans,right-left+1)
                #modifying the slidingwindow
                curr_sum-=nums[left]
                left+=1
        
        return 0 if ans==float('inf') else int(ans)



