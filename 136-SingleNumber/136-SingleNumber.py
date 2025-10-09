# Last updated: 10/8/2025, 9:52:13 PM
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=0
        for i in nums:
            a^=i
        return a

        