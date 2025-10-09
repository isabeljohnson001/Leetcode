# Last updated: 10/8/2025, 9:49:25 PM
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        left=0
        right=len(nums)-1
        max_sum=-1
        while left<right:
            curr_sum=nums[left]+nums[right]
            if curr_sum<k:
                max_sum=max(max_sum,curr_sum)
                left+=1
            else:
                right-=1
        return max_sum