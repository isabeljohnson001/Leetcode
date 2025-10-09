# Last updated: 10/8/2025, 9:51:07 PM
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = {}
        rank = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False
            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            elif rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            return True
        
        land = set()
        count = 0
        res = []
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        for r, c in positions:
            if (r, c) in land:
                res.append(count)
                continue
            land.add((r, c))
            parent[(r, c)] = (r, c)
            rank[(r, c)] = 0
            count += 1
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in land and union((r, c), (nr, nc)):
                    count -= 1
            
            res.append(count)
        
        return res