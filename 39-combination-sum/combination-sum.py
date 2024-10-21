class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(path,start,curr_sum):
            if curr_sum==target:
                ans.append(path[:])
                return ans
            
            for i in range(start,len(candidates)):
                num=candidates[i]
                if curr_sum+num<=target:
                    path.append(num)
                    backtrack(path,i,curr_sum+num)
                    path.pop()

        ans=[]
        backtrack([],0,0)
        return ans
        