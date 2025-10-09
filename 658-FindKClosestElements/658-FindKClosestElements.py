# Last updated: 10/8/2025, 9:50:00 PM
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        heap=[]
        for ar in arr:
            distance=abs(x-ar)
            heapq.heappush(heap,(-distance,-ar))
            if(len(heap)>k):
                heapq.heappop(heap)
        return sorted([-pair[1] for pair in heap])