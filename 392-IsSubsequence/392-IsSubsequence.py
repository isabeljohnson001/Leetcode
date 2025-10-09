# Last updated: 10/8/2025, 9:50:53 PM
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i=j=0

        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==len(s)