# Last updated: 10/8/2025, 9:51:13 PM
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n==0:
            return true
        visit=set()
        adj={i:[] for i in range(n)}
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)

        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei ==prev:
                    continue
                if not dfs(nei,node):
                    return False
            return True

        return dfs(0,-1) and len(visit)==n