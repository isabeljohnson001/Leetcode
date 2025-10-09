# Last updated: 10/8/2025, 9:51:55 PM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap=[-num for num in nums]
        heapq.heapify(heap)
        item=0
        while k>0:
            item=heapq.heappop(heap)
            k-=1
        return -item
        