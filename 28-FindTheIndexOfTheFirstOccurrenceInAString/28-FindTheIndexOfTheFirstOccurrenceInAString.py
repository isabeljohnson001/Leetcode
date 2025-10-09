# Last updated: 10/8/2025, 9:53:03 PM
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m=len(haystack)
        n=len(needle)
        for i in range(m-n+1):

            j=0
            while j<n and haystack[i+j]==needle[j]:
                j+=1
            if j==n:
                return i
        return -1


        