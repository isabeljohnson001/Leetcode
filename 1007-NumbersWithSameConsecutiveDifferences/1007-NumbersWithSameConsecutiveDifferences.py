# Last updated: 10/8/2025, 9:49:32 PM
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        ans=[]
        def backtrack(digit,index):

            if index==n:
                ans.append(digit)
                return

            for i in range(0,10):
                last_digit=digit%10
                if abs(last_digit-i)==k:
                    digit=digit*10
                    backtrack(digit+i,index+1)
                    digit//=10


        for i in range(1,10):
            backtrack(i,1)
        return ans

        