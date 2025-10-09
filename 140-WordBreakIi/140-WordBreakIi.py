# Last updated: 10/8/2025, 9:52:12 PM
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:  
        
        wordDict=set(wordDict)
        
        curr=[]
        cache={}
        def backtrack(i):
            if i==len(s):
                return [""]
            if i in cache:
                return cache[i]
            res=[]
            for j in range(i,len(s)):
                w=s[i:j+1]
                if w not in wordDict:
                    continue
                
                curr.append(w)
                substr=backtrack(j+1)
                for subb in substr:
                    sentence=w
                    if subb:
                        sentence+=" "+subb
                    res.append(sentence)
                cache[i]=res
                curr.pop()
            return res


        
        return backtrack(0)
      


       