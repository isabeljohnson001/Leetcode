# Last updated: 10/8/2025, 9:49:28 PM
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for  _ in range(k):
            min=heapq.heappop(nums)
            min=-min
            heapq.heappush(nums,min)
        
        return sum(nums)

        