# Last updated: 10/8/2025, 9:52:58 PM
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(curr,curr_sum,start):
            if curr_sum==target:
                ans.append(curr[:])
                return
            if curr_sum>target:
                return
            
            for i in range(start,len(candidates)):
                x=candidates[i]
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                if curr_sum+x<=target:
                    curr.append(x)
                    backtrack(curr,curr_sum+x,i+1)
                    curr.pop()

        ans=[]
        backtrack([],0,0)
        return ans