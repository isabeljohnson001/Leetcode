# Last updated: 10/8/2025, 9:48:12 PM
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist)>math.ceil(hour):
            return -1

        def check(k):
            t=0
            for d in dist:
                t=math.ceil(t)
                t+=d/k
            return t<=hour

        l,r=1,10**7

        while l<=r:
            m= (l+r)//2

            if check(m):
                r=m-1
            else:
                l=m+1
        return l
        



