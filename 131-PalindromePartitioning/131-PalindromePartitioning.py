# Last updated: 10/8/2025, 9:52:15 PM
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        memo={}
        def backtrack(curr,start):
            
            if start==len(s):
                ans.append(curr[:])
                return
            for i in range(start,len(s)):
                if isPali(start,i+1):
                    curr.append(s[start:i+1])
                    backtrack(curr,i+1)
                    curr.pop()
        def isPali(l,r):
            start,end=l,r-1
            if (start,end) in memo:
                return memo[(start,end)]
            r-=1
            while l<r:
                if s[l]!=s[r]:
                    memo[(start,end)]=False
                    return False
                l+=1
                r-=1
            memo[(start,end)]=True
            return True




        ans=[]
        backtrack([],0)
        return ans