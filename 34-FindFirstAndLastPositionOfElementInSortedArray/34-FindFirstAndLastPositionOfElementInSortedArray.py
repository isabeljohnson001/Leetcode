# Last updated: 10/8/2025, 9:53:02 PM
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findBound(isBool):
            l=0
            r=len(nums)-1
            ans=-1
            while l<=r:

                m=(l+r)//2
                
                if nums[m]==target:
                    ans=m
                    if isBool:
                        #check left
                        r=m-1
                    else:
                        #check right
                        l=m+1
                elif nums[m]>target:
                    r=m-1
                else:
                    l=m+1
            return ans

        return [findBound(True),findBound(False)]
        