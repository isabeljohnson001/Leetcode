# Last updated: 10/8/2025, 9:50:37 PM
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(node):
            for neighbour in graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    dfs(neighbour)

        n=len(isConnected)
        graph= defaultdict(list)

        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]==1:
                    graph[i].append(j)
                    graph[j].append(i)
        
        ans=0
        seen=set()
        for i in range(n):
            if i not in seen:
                seen.add(i)
                ans+=1
                dfs(i)
        return ans    