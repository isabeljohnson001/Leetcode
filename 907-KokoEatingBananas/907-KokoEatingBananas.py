# Last updated: 10/8/2025, 9:49:43 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        def calculatedHours(k):
            totalTime=0
            totalTime=sum([math.ceil(p/k) for p in piles])
            return totalTime

        l=1
        r=max(piles)
        while l<r:
            m=(l+r)//2
            if calculatedHours(m)<=h:
                r=m
            else:
                l=m+1
        return r