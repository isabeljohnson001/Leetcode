# Last updated: 10/8/2025, 9:49:21 PM
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        count=0
        basket=0
        for i in range(len(weight)):
            basket+=weight[i]
            if basket>5000:
                break
            count+=1
        return count

            
        