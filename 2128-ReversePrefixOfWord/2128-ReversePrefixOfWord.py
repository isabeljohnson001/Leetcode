# Last updated: 10/8/2025, 9:48:07 PM
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        def rev(word_list, start,end):
            
            left=start
            right=end
            while left<right:
                word_list[left],word_list[right]=word_list[right],word_list[left]
                left+=1
                right-=1
            return "".join(word_list)

        word_list=list(word)
        end_index=0
        for i in range(len(word_list)):
            if word_list[i]==ch:
                end_index=i
                break
        rev(word_list,0, end_index)
        return "".join(word_list)

        

        