# Last updated: 10/8/2025, 9:48:05 PM
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
  
        def dfs(node):
            if node==destination:
                return True
            for neighbour in graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    if dfs(neighbour):
                        return True
            return False


        graph=defaultdict(list)
        for [i,j] in edges:
            graph[i].append(j)
            graph[j].append(i)

        seen={source}
        return dfs(source)