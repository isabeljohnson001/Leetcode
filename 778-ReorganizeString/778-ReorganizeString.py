# Last updated: 10/8/2025, 9:49:52 PM
class Solution:
    def reorganizeString(self, s: str) -> str:

        count=Counter(s)
        maxHeap=[(-count, char) for char,count in count.items()]
        heapq.heapify(maxHeap)
        res=""
        while maxHeap:

            count,char=heapq.heappop(maxHeap)
            if len(res)>0 and res[-1]==char:
                if not maxHeap:
                    break
                count2,char2=heapq.heappop(maxHeap)
                res+=char2
                count2+=1
                if count2:
                    heapq.heappush(maxHeap,(count2,char2))
                heapq.heappush(maxHeap,(count,char))
            else:
                res+=char
                count+=1
                if count:
                    heapq.heappush(maxHeap,(count,char))
        return res if len(res)==len(s) else ""
        