# Last updated: 10/8/2025, 9:53:07 PM
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result=set()
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                left,right=j+1,n-1
                while left<right:
                        curr_sum=nums[i]+nums[j]+nums[left]+nums[right]
                        if curr_sum==target:
                            curr_quad=tuple((nums[i],nums[j],nums[left],nums[right]))
                            if curr_quad not in result:
                                result.add(curr_quad)
                        if curr_sum<target:
                            left+=1
                        else:
                            right-=1
        result_list=[list(quad) for quad in result]
        return result_list        
                                