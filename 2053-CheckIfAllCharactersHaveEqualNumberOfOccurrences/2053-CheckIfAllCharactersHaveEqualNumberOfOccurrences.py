# Last updated: 10/8/2025, 9:48:08 PM
from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq=Counter(s)

        return len(set(freq.values()))==1



            