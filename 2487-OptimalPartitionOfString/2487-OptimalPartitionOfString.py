# Last updated: 10/8/2025, 9:47:47 PM
class Solution:
    def partitionString(self, s: str) -> int:

        charSet=set()
        res=1

        for c in s:
            if c in charSet:
                res+=1
                charSet=set()
            charSet.add(c)
        return res
        