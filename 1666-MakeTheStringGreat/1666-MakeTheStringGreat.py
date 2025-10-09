# Last updated: 10/8/2025, 9:48:52 PM
class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        
        for c in s:
            
            #"leEeetcode"
            if stack and stack[-1]!=c and stack[-1].upper()==c.upper():
                    stack.pop()
                    continue
                
            stack.append(c)
        return "".join(stack)
        