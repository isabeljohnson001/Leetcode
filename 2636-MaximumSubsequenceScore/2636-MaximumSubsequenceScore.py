# Last updated: 10/8/2025, 9:47:42 PM
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:

        pairs=[(n1,n2) for n1,n2 in zip(nums1,nums2)]
        pairs.sort(key=lambda x:x[1],reverse=True)
        minHeap=[]
        n1Sum=0
        res=0
        for n1,n2 in pairs:
            n1Sum+=n1
            heapq.heappush(minHeap,n1)

            while len(minHeap)>k:
                pop_item=heapq.heappop(minHeap)
                n1Sum-=pop_item
            if len(minHeap)==k:
                res=max(res,n1Sum*n2)
        return res  
        