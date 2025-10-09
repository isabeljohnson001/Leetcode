# Last updated: 10/8/2025, 9:47:59 PM
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dp(i):
            if i>=len(questions):
                return 0
            
            j=i+questions[i][1]+1
            return max(questions[i][0]+dp(j),dp(i+1))
        return dp(0)