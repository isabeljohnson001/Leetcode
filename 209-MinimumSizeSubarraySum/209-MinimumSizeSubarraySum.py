# Last updated: 10/8/2025, 9:51:57 PM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len=float("inf")
        curr_sum=0
        count=0
        left=0
        for right in range(len(nums)):
            curr_sum+=nums[right]
            count+=1
            while curr_sum>=target:
                min_len=min(min_len,count)
                curr_sum-=nums[left]
                left+=1
                count-=1
        return min_len if min_len !=float("inf") else 0

      



