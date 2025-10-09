# Last updated: 10/8/2025, 9:47:57 PM
import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total_sum=sum(nums)
        target=total_sum/2
        curr_sum=total_sum
        i=0
        numbers=[-num for num in nums]
        heapq.heapify(numbers)
        while curr_sum>target:
            curr_half=-heapq.heappop(numbers)/2
            curr_sum-=curr_half
            heapq.heappush(numbers,-curr_half)
            i+=1
        return i
        
