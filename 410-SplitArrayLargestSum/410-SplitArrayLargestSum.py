# Last updated: 10/8/2025, 9:50:50 PM
from itertools import combinations
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n=len(nums)

        if k==1:
            return sum(nums)
        if k==n:
            return max(nums)
        def partNeeded(sumReq):
            curr_sum=0
            parts=1
            for i in range(len(nums)):
                if curr_sum+nums[i]>sumReq:
                    parts+=1
                    curr_sum=0
                curr_sum+=nums[i]
            return parts

        l=max(nums)
        r=sum(nums)
        while l<r:
            m=(l+r)//2
            if partNeeded(m)<=k:
                r=m
            else:
                l=m+1
        return r