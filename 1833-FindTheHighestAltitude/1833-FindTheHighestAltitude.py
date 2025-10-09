# Last updated: 10/8/2025, 9:48:47 PM
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix=[0]
        for i in range(len(gain)):
            prefix.append(prefix[-1]+gain[i])
        return max(prefix)

        