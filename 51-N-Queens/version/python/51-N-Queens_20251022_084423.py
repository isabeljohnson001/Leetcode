# Last updated: 10/22/2025, 8:44:23 AM
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        boards=[["."]*n for _ in range(n)]
        col=set()
        posDia=set()
        negDia=set()

        def backtrack(r):
            if r==n:
                res.append(["".join(i) for i in boards])

            for c in range(n):

                if c in col or (r+c) in posDia or (r-c) in negDia:
                    continue
                col.add(c)
                posDia.add(r+c)
                negDia.add(r-c)
                boards[r][c]="Q"
                backtrack(r+1)
                col.remove(c)
                posDia.remove(r+c)
                negDia.remove(r-c)
                boards[r][c]="."


        backtrack(0)
        return res