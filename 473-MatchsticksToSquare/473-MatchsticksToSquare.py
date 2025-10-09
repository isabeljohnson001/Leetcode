# Last updated: 10/8/2025, 9:50:46 PM
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        if sum(matchsticks)%4!=0:
            return False
        
        matchsticks.sort(reverse=True)
        target=sum(matchsticks)//4
        if matchsticks[0]>target:
            return False
        sides=[0]*4
        def backtrack(i):
            if i==len(matchsticks):
                return True
            
            
            for j in range(4):
                if sides[j]+matchsticks[i]<=target:
                    sides[j]+=matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[j]-=matchsticks[i]
            return False
        return backtrack(0)

