class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:


        text_list=defaultdict(int)
        pattern_list=defaultdict(int)
        search="balloon"
        
        for i in text:
            if i not in text_list:
                text_list[i]=0
            text_list[i]+=1
        for i in search:
            if i not in pattern_list:
                pattern_list[i]=0
            pattern_list[i]+=1

        result=float("inf")
        for char in pattern_list:
            if char in text_list:
                result=min(result,text_list[char]//pattern_list[char])
            else:
                result=0
        return result


        