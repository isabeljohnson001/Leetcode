# Last updated: 10/8/2025, 9:48:56 PM
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix=[nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[-1]+nums[i])
        return prefix
        