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
        '''

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



        