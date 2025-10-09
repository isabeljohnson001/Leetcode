# Last updated: 10/8/2025, 9:52:16 PM
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        #creat an adj list:
        adj=defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j]+"*"+word[j+1:]
                adj[pattern].append(word)

        visit=set()
        visit.add(beginWord)
        q=deque([beginWord])
        res=1
        while q:
            for i in range(len(q)):
                word=q.popleft()
                if word==endWord:
                    return res
                visit.add(word)
                for j in range(len(word)):
                    pattern=word[:j]+"*"+word[j+1:]
                    for nei in adj[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            res+=1
        return 0

        