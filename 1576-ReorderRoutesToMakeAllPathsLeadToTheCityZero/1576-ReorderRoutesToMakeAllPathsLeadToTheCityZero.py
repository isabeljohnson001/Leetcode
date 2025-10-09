# Last updated: 10/8/2025, 9:48:55 PM
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        visit=set()
        roads=set()
        changes=0

        adj={nei:[] for nei in range(n)}

        for x,y in connections:
            adj[x].append(y)
            adj[y].append(x)
            roads.add((x,y))

        def dfs(city):
            nonlocal roads,visit,adj,changes 

            for nei in adj[city]:
                if nei in visit:
                    continue
                if (nei,city) not in roads:
                    changes+=1
                visit.add((city))
                dfs(nei)

        visit.add(0)
        dfs(0)

        return changes



