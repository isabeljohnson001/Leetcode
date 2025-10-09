# Last updated: 10/8/2025, 9:50:51 PM
class Solution:
    def longestPalindrome(self, s: str) -> int:

        char_Set=set()
        res=0

        for c in s:
            if c in char_Set:
                char_Set.remove(c)
                res+=2
            else:
                char_Set.add(c)
        if len(char_Set)!=0:
            res+=1
        return res
        