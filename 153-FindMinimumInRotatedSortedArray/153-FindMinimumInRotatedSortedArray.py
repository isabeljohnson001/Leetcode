# Last updated: 10/8/2025, 9:52:07 PM
class Solution:
    def findMin(self, nums: List[int]) -> int:

        l,r=0,len(nums)-1

        if nums[l]<nums[r] or len(nums)==1:
            return nums[l]

        while l<=r:

            m=(l+r)//2
            if nums[m]>nums[r]:
                l=m+1
            elif nums[m]<nums[r]:
                r=m
            else:
                r=r-1
        return nums[l]
