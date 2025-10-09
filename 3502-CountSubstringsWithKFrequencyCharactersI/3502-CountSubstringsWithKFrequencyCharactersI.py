# Last updated: 10/8/2025, 9:47:35 PM
from collections import Counter
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:

        '''ans=0
        substrings=[]
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                curr_str=s[i:j]
                counts_ch=Counter(curr_str)
                if any(i>=k for i in counts_ch.values()):
                    ans+=1
        return ans
        
        ans=0
        n=len(s)
        for i in range(n):
            counts=Counter()
            for j in range(i,n):
                counts[s[j]]+=1
                if counts[s[j]]>=k:
                    ans+=n-j
                    break
        return ans
        '''
        '''
        # Using sliding window approach
        n=len(s)
        res=0
        for left in range(n):
            freq={}
            maxFreq=0
            for right in range(left,n):
                char=s[right]
                freq[char]=freq.get(char,0)+1
                max_freq=max(maxFreq,freq[char])
                if max_freq>=k:
                    res+=n-right
        return res
        '''

        ans=0
        l=0
        freq={}
        for c in s:
            freq[c]=freq.get(c,0)+1
            while freq[c]==k:
                freq[s[l]]-=1
                l=l+1
            ans+=l
        return ans




        