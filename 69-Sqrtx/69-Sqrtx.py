# Last updated: 10/8/2025, 9:52:51 PM
class Solution:
    def mySqrt(self, x: int) -> int:

        if x<2:
            return x

        l,r=2,(x//2)
        while l<=r:
            pivot=(l+r)//2
            num=pivot*pivot
            if num==x:
                return pivot
            elif num>x:
                r=pivot-1
            else:
                l=pivot+1
        return r

        