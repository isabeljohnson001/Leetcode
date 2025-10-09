# Last updated: 10/8/2025, 9:49:39 PM
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        s_list=list(s)
        left=0
        right=len(s_list)-1
        while(left<right):
            while left<right and not s[left].isalpha():
                left+=1
            while left<right and not s[right].isalpha():
                right-=1
            
            s_list[left],s_list[right]=s_list[right],s_list[left]
            left+=1
            right-=1
        return "".join(s_list)
        