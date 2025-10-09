# Last updated: 10/8/2025, 9:52:46 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m=len(matrix)
        n=len(matrix[0])

        l,r=0,m*n-1

        while l<=r:
            m=(l+r)//2

            row=m//n
            col=m%n

            num=matrix[row][col]
            if num==target:
                return True
            elif num<target:
                l=m+1
            else:
                r=m-1
        return False