# Last updated: 10/8/2025, 9:51:51 PM
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def backtrack(start,path,curr_sum):
            if len(path)==k:
                if curr_sum==n:
                    ans.append(path[:])
                return

            if curr_sum>n:
                return
            
            for i in range(start,10):
                    if curr_sum+i<=n:
                        path.append(i)
                        backtrack(i+1,path,curr_sum+i)
                        path.pop()




        ans=[]
        backtrack(1,[],0)
        return ans
        