from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts=Counter(nums)
        return next(num for num, count in counts.items() if count==1)
        