# Last updated: 10/8/2025, 9:49:24 PM
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap=[stick for stick in sticks]
        heapq.heapify(heap)
        cost=0
        while len(heap)>1:
            stick1, stick2=heapq.heappop(heap),heapq.heappop(heap)
            sum=stick1+stick2
            cost+=sum
            heapq.heappush(heap,sum)
        return cost
        