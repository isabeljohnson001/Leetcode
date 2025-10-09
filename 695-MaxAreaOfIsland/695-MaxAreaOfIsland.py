# Last updated: 10/8/2025, 9:49:58 PM
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows=len(grid)
        cols=len(grid[0])
        maxArea=0
        ans=0
        visit=set()
        directions=[(0,1),(0,-1),(1,0),(-1,0)]

        def isValid(r,c):
            if 0<=r<rows and 0<=c<cols and grid[r][c]==1: return True
        def area(r,c):
            if not isValid(r,c) or (r,c) in visit:
                return 0
            visit.add((r,c))
            return 1+area(r,c+1)+area(r,c-1)+area(r+1,c)+area(r-1,c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    maxArea=max(maxArea,area(r,c))

        return maxArea