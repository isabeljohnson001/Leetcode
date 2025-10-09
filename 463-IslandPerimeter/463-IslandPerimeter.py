# Last updated: 10/8/2025, 9:50:47 PM
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        visit=set()

        def dfs(r,c):
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]==0:
                return 1
            if (r,c) in visit:
                return 0
            
            visit.add((r,c))
            res=dfs(r+1,c)
            res+=dfs(r-1,c)
            res+=dfs(r,c+1)
            res+=dfs(r,c-1)

            return res

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return dfs(i,j)