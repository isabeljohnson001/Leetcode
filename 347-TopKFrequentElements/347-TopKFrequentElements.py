# Last updated: 10/8/2025, 9:50:59 PM
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        heap=[]
        for key,value in count.items():
            heapq.heappush(heap,(value,key))
            if len(heap)>k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]




        