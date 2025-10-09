# Last updated: 10/8/2025, 9:48:48 PM
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        arr=['a']*n

        k=k-n
        i=n-1
        while k>0:
            if k<25:
                arr[i]=chr(ord('a')+k)
                k=0
            else:
                arr[i]='z'
                k=k-25
                i-=1
        return "".join(arr)

        