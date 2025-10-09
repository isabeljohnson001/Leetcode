# Last updated: 10/8/2025, 9:49:56 PM
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum=sum(nums)
        left_sum=0

        for i in range(len(nums)):
            if (2*left_sum)+nums[i]==total_sum:
                return i
            left_sum+=nums[i]
        return -1
        