# Last updated: 10/8/2025, 9:50:49 PM
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        


        if startGene==endGene:
            return 0
        queue=collections.deque()
        queue.append((startGene,0))
        seen={startGene}
        while queue:
            current_Gene,steps=queue.popleft()
            if current_Gene ==endGene:
                return steps
            for c in "ACGT":
                for i in range(len(current_Gene)):
                    neighbour=current_Gene[:i]+c+current_Gene[i+1:]
                    if neighbour not in seen and neighbour in bank:
                        seen.add(neighbour)
                        queue.append((neighbour,steps+1))
        return -1