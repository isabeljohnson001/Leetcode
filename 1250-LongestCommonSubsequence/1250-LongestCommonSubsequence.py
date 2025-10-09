# Last updated: 10/8/2025, 9:49:17 PM
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @cache

        def dp(i,j):
            if i==-1 or j==-1:
                return 0

            if text1[i] == text2[j]:
                return 1+dp(i-1,j-1)
            
            return max(dp(i-1,j),dp(i,j-1))
        
        return dp(len(text1)-1,len(text2)-1)
        