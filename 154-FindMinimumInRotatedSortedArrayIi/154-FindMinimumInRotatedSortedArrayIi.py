# Last updated: 10/8/2025, 9:52:07 PM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l=0
        r=len(nums)-1
        res=nums[0]
        if len(nums)==1 or nums[l]<nums[r]:
                return nums[l]
        while l<=r:

            m=(l+r)//2
            
            #left sorted array - so the search elements will be in right half
            if nums[m]<nums[r]:
                r=m
            elif nums[m]>nums[r]:
                l=m+1
            else:
                r=r-1
        return nums[l]




