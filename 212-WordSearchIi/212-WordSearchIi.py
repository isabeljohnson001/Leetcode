# Last updated: 10/8/2025, 9:51:53 PM
class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False

    def addWord(self,word):
        cur=self
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.endOfWord=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows,cols=len(board),len(board[0])
        res,visit=set(),set()

        root=TrieNode()
        for word in words:
            root.addWord(word)
        
        def dfs(r,c,node,word):
            if r<0 or c<0 or r==rows or c==cols or board[r][c] not in node.children or (r,c) in visit:
                return
            visit.add((r,c))
            node=node.children[board[r][c]]
            word+=board[r][c]
            if node.endOfWord:
                res.add(word)

            directions={(0,1),(0,-1),(1,0),(-1,0)}
            for dx,dy in directions:
                newRow,newCol=r+dx,c+dy
                dfs(newRow,newCol,node,word)
            visit.remove((r,c))
            
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")
        return list(res)

