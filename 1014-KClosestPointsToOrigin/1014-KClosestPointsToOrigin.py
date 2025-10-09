# Last updated: 10/8/2025, 9:49:34 PM
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap=[]
        for x,y in points:
            
            sqr=x**2+y**2
            heapq.heappush(heap,(-sqr,[x,y]))
            while len(heap)>k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]
                
        
        
        