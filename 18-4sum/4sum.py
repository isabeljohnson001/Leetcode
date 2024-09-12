class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result=set()

        n=len(nums)

        for i in range(n):
            #if i>0 and nums[i]==nums[i-1]:
            #    continue
            for j in range(i+1,n):
                #if j>0 and nums[j]==nums[j-1]:
                #    continue
                left,right=j+1,n-1
                while left<right:
                    current_sum=nums[i]+nums[j]+nums[left]+nums[right]
                    if current_sum==target:
                        current_quad=tuple((nums[i],nums[j],nums[left],nums[right]))
                        if current_quad not in result:
                            result.add(current_quad)
                        #while left<right and nums[left]==nums[left+1]:
                        #    left+=1
                        #while left<right and nums[right]==nums[right-1]:
                        #    right-=1
                    if current_sum<target:
                        left+=1
                    else:
                        right-=1
        result_list=[list(quad) for quad in result]
        return result_list                
                




        