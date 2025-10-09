# Last updated: 10/8/2025, 9:53:01 PM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while(l<=r):
            m=(l+r)//2
            if nums[m]==target:
                return m
            elif nums[m]>target:
                r=m-1
            else:
                l=m+1
        return l