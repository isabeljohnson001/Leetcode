class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        s_list=list(s)
        left=0
        right=len(s_list)-1
        while(left<right):
            #if s_list not in ('\\','\\'')
            while left<right and not s[left].isalpha():
                left+=1
            while left<right and not s[right].isalpha():
                right-=1
            
            s_list[left],s_list[right]=s_list[right],s_list[left]
            left+=1
            right-=1
        return "".join(s_list)
        