class Solution:
    def countSubstrings(self, s: str) -> int:
        res=[]
        def ifPalindrome(right,left):
            while left<=right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        for i in range(len(s)):

            l,r=i,i
            temp=""
            while l>=0 and r<len(s) and s[r]==s[l]:
                temp=s[l:r+1]
                res.append(temp)
                l-=1
                r+=1
            
            l,r=i,i+1
            temp=""
            while l>=0 and r<len(s) and s[r]==s[l]:
                temp=s[l:r+1]
                res.append(temp)
                l-=1
                r+=1
        return len(res)
            


        