# Last updated: 10/8/2025, 9:50:54 PM
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count=collections.Counter(s)
        for id,value in enumerate(s):
            if count[value]==1:
                return id
        return -1
        