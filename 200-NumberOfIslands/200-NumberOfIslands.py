# Last updated: 10/8/2025, 9:51:59 PM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def isValid(row,col):
            return 0<=row<m and 0<=col<n and grid[row][col]=="1"



        def dfs(row,col):
            for dx,dy in directions:
                nextRow, nextCol=row+dy,col+dx
                if isValid(nextRow,nextCol) and (nextRow,nextCol) not in seen: 
                    seen.add((nextRow,nextCol))
                    dfs(nextRow,nextCol)




        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        m=len(grid)
        n=len(grid[0])
        seen=set()
        ans=0

        for row in range(m):
            for col in range(n):
                if grid[row][col]=="1" and (row,col) not in seen:
                    ans+=1
                    seen.add((row,col))
                    dfs(row,col)
        return ans


        