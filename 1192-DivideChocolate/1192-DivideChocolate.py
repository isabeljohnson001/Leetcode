# Last updated: 10/8/2025, 9:49:17 PM
class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:

        def cutChunks(m):
            chunks = 0
            current_sweetness = 0
            for item in sweetness:
                current_sweetness += item

                if current_sweetness >= m:
                    chunks += 1
                    current_sweetness = 0
            return chunks

        l = 1
        r = sum(sweetness)//(k+1)
        while l < r:
            mid = (l + r+1) // 2
            chunks = cutChunks(mid)
            if chunks >= k + 1:
                l = mid
            else:
                r = mid - 1
        return l
