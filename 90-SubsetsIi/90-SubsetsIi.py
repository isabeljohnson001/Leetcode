# Last updated: 10/8/2025, 9:52:36 PM
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtrack(curr, start):
            if start>len(nums):
                return
            
            ans.append(curr[:])
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                curr.append(nums[i])
                backtrack(curr,i+1)
                curr.pop()

        ans=[]
        backtrack([],0)
        return ans