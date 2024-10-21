class Solution:
    def totalNQueens(self, n: int) -> int:


        def backtrack(row,daigonals,anti_daigonals,cols):
            if row ==n:
                return 1

            solutions=0
            for col in range(n):
                daigonal=row-col
                anti_daigonal=row+col

                if(col in cols or daigonal in daigonals or anti_daigonal in anti_daigonals):
                    continue
                cols.add(col)
                daigonals.add(daigonal)
                anti_daigonals.add(anti_daigonal)

                solutions+=backtrack(row+1,daigonals,anti_daigonals,cols)

                cols.remove(col)
                daigonals.remove(daigonal)
                anti_daigonals.remove(anti_daigonal)
            
            return solutions
        
        return backtrack(0,set(),set(),set())
        