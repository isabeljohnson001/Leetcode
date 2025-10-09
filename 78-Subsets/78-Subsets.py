# Last updated: 10/8/2025, 9:52:44 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(curr,start):
            if start>len(nums):
                return

            ans.append(curr[:])
            for i in range(start,len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    backtrack(curr,i+1)
                    curr.pop()

        ans=[]
        backtrack([],0)
        return ans