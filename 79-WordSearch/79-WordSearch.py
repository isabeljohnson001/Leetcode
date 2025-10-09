# Last updated: 10/8/2025, 9:52:43 PM
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        dir={(0,-1),(0,1),(1,0),(-1,0)}
        def isValid(r,c):
            return 0<=r<rows and 0<=c<cols

        def backtrack(r,c,visited,startIndex):
            if startIndex==len(word):
                return True


            for dx,dy in dir:
                newRow=r+dx
                newCol=c+dy
                if isValid(newRow,newCol) and (newRow,newCol) not in visited:

                    if board[newRow][newCol]!=word[startIndex]:
                        continue
                    else:
                        visited.add((newRow,newCol))
                        if backtrack(newRow,newCol,visited,startIndex+1):
                            return True
                        visited.remove((newRow,newCol))
            return False
                
        word_count=Counter(word)
        board_count=Counter(c for r in board for c in r)

        if any(word_count[ch]>board_count.get(ch,0) for ch in word_count):
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c]==word[0] and backtrack(r,c,{(r,c)},1):
                    return True
        return False

        




