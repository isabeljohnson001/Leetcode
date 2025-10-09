# Last updated: 10/8/2025, 9:49:19 PM
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1]) 
        print(trips)
        totalPass=0
        minHeap=[] #drop off,noofpassengers
        for trip in trips:
            numPass,start,end=trip
            while minHeap and minHeap[0][0]<=start:
                totalPass-=minHeap[0][1]
                heapq.heappop(minHeap)
            totalPass+=numPass
            if totalPass>capacity:
                return False
            heapq.heappush(minHeap,[end,numPass])
        return True
            
        