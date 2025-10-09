# Last updated: 10/8/2025, 9:48:49 PM
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        i=0
        maxHeap=[]
        for i in range(len(heights)-1):
            diff=heights[i+1]-heights[i]
            if diff<=0:
                continue
            
            bricks-=diff
            heapq.heappush(maxHeap,-diff)
            if bricks<0:
                if ladders==0:
                    return i
                else:
                    ladders-=1
                    bricks+=-heapq.heappop(maxHeap)
                
        return len(heights)-1
        