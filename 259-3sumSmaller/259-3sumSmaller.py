# Last updated: 10/8/2025, 9:51:14 PM
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        nums.sort()
        ans=0
        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            need=target-nums[i]
            while l<r:
                if nums[l]+nums[r]<need:
                    ans+=r-l
                    l+=1
                
                else:
                    r-=1
        return ans