# Last updated: 10/8/2025, 9:47:35 PM
class Solution:
    def stringSequence(self, target: str) -> List[str]:

        n=len(target)

        result=[]
        current_str=[""]*n

        for i in range(n):

            current_str[i]="a"
            for ch in range(ord("a"),ord(target[i])+1):
                current_str[i]=chr(ch)

                result.append("".join(current_str))

        return result