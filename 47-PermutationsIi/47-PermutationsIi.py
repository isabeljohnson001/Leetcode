# Last updated: 10/8/2025, 9:52:56 PM
from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        hash=Counter(nums)

        def backtrack(curr):
            if len(curr)==len(nums):
                ans.append(curr[:])
                return

            for i in hash:
                if hash[i]<=0:
                    continue
                hash[i]-=1
                curr.append(i)
                backtrack(curr)
                curr.pop()
                hash[i]+=1




        

        ans=[]
        backtrack([])
        return ans
        