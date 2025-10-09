# Last updated: 10/8/2025, 9:52:45 PM
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtrack(curr,start):
            if len(curr)==k:
                ans.append(curr[:])
                return
            
            for i in range(start,n-(k-len(curr))+2):
                if i not in curr:
                    curr.append(i)
                    backtrack(curr,i+1)
                    curr.pop()
        ans=[]
        backtrack([],1)
        return ans