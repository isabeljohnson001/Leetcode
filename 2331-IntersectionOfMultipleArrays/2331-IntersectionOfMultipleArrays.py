# Last updated: 10/8/2025, 9:47:56 PM
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        seen=set(nums[0])
        for i in nums[1:]:
            seen&=set(i)

        return sorted(seen)
        