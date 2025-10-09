# Last updated: 10/8/2025, 9:48:53 PM
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:


        count=Counter(arr)

        ordered=sorted(count.values(),reverse=True)

        while k:
            val=ordered[-1]
            if val<=k:
                k-=val
                ordered.pop()
            else:
                break
        return len(ordered)