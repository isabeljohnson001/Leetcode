# Last updated: 10/8/2025, 9:52:52 PM
class Solution:
    def totalNQueens(self, n: int) -> int:


        count=0
        cols=set()
        posDia=set()
        negDia=set()
        boards=[["."]*n for _ in range(n)]
        def backtrack(r):
            if r==n:
                nonlocal count
                count+=1
            for c in range(n):
                if c in cols or (r+c) in posDia or (r-c) in negDia:
                    continue
                cols.add(c)
                posDia.add(r+c)
                negDia.add(r-c)
                boards[r][c]="Q"
                backtrack(r+1)
                cols.remove(c)
                posDia.remove(r+c)
                negDia.remove(r-c)
                boards[r][c]="."


        backtrack(0)
        return count