# Last updated: 10/8/2025, 9:52:57 PM
import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used=[False]*len(nums)
        def backtrack(curr):
            if len(curr)==len(nums):
                ans.append(curr[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                curr.append(nums[i])
                used[i]=True
                backtrack(curr)
                curr.pop()
                used[i]=False



        ans=[]
        backtrack([])
        return ans