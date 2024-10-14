class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        #create adjany list
        #do bfs

        adj=collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern=word[:j]+"*"+word[j+1:]
                adj[pattern].append(word)
        
        visit=set([beginWord])
        queue=deque([beginWord])
        res=1
        while queue:
            for i in range(len(queue)):
                current=queue.popleft()
                if current==endWord:
                    return res
                for j in range(len(current)):
                    pattern=current[:j]+"*"+current[j+1:]
                    for nei in adj[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            queue.append(nei)
            res+=1
        return 0

        