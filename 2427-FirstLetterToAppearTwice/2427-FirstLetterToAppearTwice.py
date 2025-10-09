# Last updated: 10/8/2025, 9:47:52 PM
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen=set()
        for ch in s:
            if ch in seen:
                return ch
            seen.add(ch)
