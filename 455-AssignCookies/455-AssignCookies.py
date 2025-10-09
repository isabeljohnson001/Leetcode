# Last updated: 10/8/2025, 9:50:48 PM
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()

        i=0
        j=0
        while i<len(g):

            while j<len(s) and g[i]>s[j]:
                j+=1
            if j<len(s):
                i+=1
                j+=1
            else:
                break
        return i

        