# Last updated: 10/8/2025, 9:51:16 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])


        for i in range(m):

            l=0
            r=n-1

            while l<=r:
                m=(l+r)//2
                num=matrix[i][m]
                if num==target:
                    return True
                elif num<target:
                    l=m+1
                else:
                    r=m-1
        return False