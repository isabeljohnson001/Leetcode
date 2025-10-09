# Last updated: 10/8/2025, 9:49:14 PM
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        #Input: text = "nlaebolko"
        from collections import Counter
        #balloon
        count=Counter(text)
        count_baloon=Counter("balloon")
        
        return min(count[c]//count_baloon[c] for c in count_baloon) 
        
                
        