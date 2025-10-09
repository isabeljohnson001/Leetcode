# Last updated: 10/8/2025, 9:47:58 PM
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:

        res=[]
        if finalSum%2:
            return res
        currSum=0
        currNum=2

        while currSum<finalSum:
            currSum+=currNum
            res.append(currNum)
            currNum+=2
            
        if currSum==finalSum:
            return res
        else:
            res.pop(res.index(currSum-finalSum))
        return res
        


        