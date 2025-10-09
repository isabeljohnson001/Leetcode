# Last updated: 10/8/2025, 9:47:44 PM
class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:

        def sum_of_digits(n):

            tot=0
            while n:
                tot+=n%10
                n//=10
            return tot

        original=n
        count=0
        while sum_of_digits(n)>target:
            n=n//10+1
            count+=1
        return n*(10**count)-original
        