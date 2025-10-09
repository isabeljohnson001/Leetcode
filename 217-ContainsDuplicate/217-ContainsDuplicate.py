# Last updated: 10/8/2025, 9:51:52 PM

from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts=Counter(nums)
        return any(count>1 for count in counts.values())
        
        