class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        ans=1
        def dfs(node):
            nonlocal ans
            for neighbour in graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    ans+=1
                    dfs(neighbour)
        
        graph=defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

        seen={0}
        for node in restricted:
            seen.add(node)
        dfs(0)
        return ans
        
        