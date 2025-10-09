# Last updated: 10/8/2025, 9:49:09 PM
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        costs=[ abs(ord(sc)-ord(st)) for sc,st in zip(s,t)]

        left=0
        curr=0
        ans=0
        for right in range(len(costs)):
            curr+=costs[right]

            while curr>maxCost:
                curr-=costs[left]
                left+=1
            ans=max(ans,(right-left)+1)
        return ans
        