# Last updated: 10/8/2025, 9:52:54 PM
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        boards=[["."]*n for _ in range(n)]
        cols=set()
        posDia=set()
        negDia=set()

        def backtrack(r):
            if r==n:
                res.append(["".join(r) for r in boards])
                
            for c in range(n):

                if c in cols or r-c in negDia or r+c in posDia:
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
        return res