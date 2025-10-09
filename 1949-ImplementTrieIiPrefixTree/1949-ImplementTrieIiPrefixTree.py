# Last updated: 10/8/2025, 9:48:45 PM
class TrieNode:
    def __init__(self):
        self.children={}
        self.endofword=False
        self.countWord=0
        self.countPrefix=0
class Trie:

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
            cur.countPrefix+=1
        cur.countWord+=1


    def countWordsEqualTo(self, word: str) -> int:
        cur=self.root
        for c in word:
            if c not in cur.children:
                return 0
            cur=cur.children[c]
        return cur.countWord

    def countWordsStartingWith(self, prefix: str) -> int:
        cur=self.root
        for c in prefix:
            if c not in cur.children:
                return 0
            cur=cur.children[c]
        return cur.countPrefix

    def erase(self, word: str) -> None:
        cur=self.root
        stack=[]
        for c in word:
            if c not in cur.children:
                return 0
            stack.append([cur,c])
            cur=cur.children[c]
        cur.countWord-=1
        for node,c in  stack:
            node.children[c].countPrefix-=1


        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)