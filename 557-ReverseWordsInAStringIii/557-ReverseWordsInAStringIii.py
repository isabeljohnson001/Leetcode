# Last updated: 10/8/2025, 9:50:35 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        ans=[]
        def reverse(word):
            word_list=list(word)
            left=0
            right=len(word_list)-1
            while left<right:
                word_list[left],word_list[right]=word_list[right],word_list[left]
                left+=1
                right-=1
            return "".join(word_list)

        words=s.split(' ')
        for item in words:
            ans.append(reverse(item))
        return " ".join(ans)


        