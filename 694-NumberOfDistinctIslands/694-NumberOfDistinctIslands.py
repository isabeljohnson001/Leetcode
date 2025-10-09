# Last updated: 10/8/2025, 9:49:59 PM
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def isValid(r,c):
            return 0<=r<rows and 0<=c<cols and grid[r][c]==1
        directions=[(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r,c,r0,c0,shape):
            if not isValid(r,c) or (r,c) in visit:
                return 0
            visit.add((r,c))
            shape.append((r-r0,c-c0))
            for dx,dy in directions:
                dfs(r+dx,c+dy,r0,c0,shape)

             
        rows=len(grid)
        cols=len(grid[0])
        visit=set()
        unique=set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    shape=[]
                    dfs(r,c,r,c,shape)
                    unique.add(tuple(shape))
        return len(unique)
                    
        

        