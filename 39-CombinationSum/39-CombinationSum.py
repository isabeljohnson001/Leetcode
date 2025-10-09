# Last updated: 10/8/2025, 9:52:59 PM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(curr,start,curr_sum):
            if curr_sum==target:
                ans.append(curr[:])
                return
            if curr_sum>target:
                return
            
            for i in range(start,len(candidates)):
                x=candidates[i]
                if curr_sum+x<=target:
                    curr.append(x)
                    backtrack(curr,i,curr_sum+x)
                    curr.pop()


        ans=[]
        backtrack([],0,0)
        return ans