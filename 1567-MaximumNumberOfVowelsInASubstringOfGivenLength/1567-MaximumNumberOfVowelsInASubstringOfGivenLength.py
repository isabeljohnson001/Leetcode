# Last updated: 10/8/2025, 9:48:57 PM
class Solution:
    def maxVowels(self, s: str, k: int) -> int:


        ans=0
        curr=0
        vowels={"a","e","i","o","u"}
        for i in range(k):
            if s[i] in vowels:
                curr+=1
        ans=curr
        left=0
        for right in range(k,len(s)):
            if s[left] in vowels:
                curr-=1

            if s[right] in vowels:
                curr+=1
            ans=max(ans,curr)
            left+=1
        return ans

