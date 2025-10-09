# Last updated: 10/8/2025, 9:48:50 PM
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:



        def valid(row, col):
            return 0<=row<n and 0<=col<m

        def check(effort):
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            seen = {(0, 0)}
            stack = [(0, 0)]
            while stack:
                row, col = stack.pop()
                if (row, col) == (n-1, m-1):
                    return True
                for dx, dy in directions:
                    next_row, next_col = row + dy, col + dx
                    if valid(next_row, next_col) and (next_row, next_col) not in seen:
                        if abs(heights[next_row][next_col] - heights[row][col]) <= effort:
                            seen.add((next_row, next_col))
                            stack.append((next_row, next_col))
            return False



        #n=len(heights)
        #m=len(heights[0])
        n, m = len(heights), len(heights[0])
        #l=0
        #r=max(max(row) for row in heights)
        l, r = 0, max(max(row) for row in heights)
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
        