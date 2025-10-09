# Last updated: 10/8/2025, 9:51:05 PM
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        

        adj={i:[] for i in range(n)}
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)

        def dfs(i):

            for nei in adj[i]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)



        visit=set()
        ans=0
        for i in range(n):
            if i not in visit:
                visit.add(i)
                ans+=1
                dfs(i)
        return ans
