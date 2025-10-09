# Last updated: 10/8/2025, 9:48:08 PM
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap=[-pile for pile in piles]
        heapq.heapify(heap)
        
        while k>0:
            item=heapq.heappop(heap)
            heapq.heappush(heap,math.floor(item/2))
            k-=1
        return -sum(heap)