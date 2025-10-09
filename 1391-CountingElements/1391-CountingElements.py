# Last updated: 10/8/2025, 9:49:10 PM
class Solution:
    def countElements(self, arr: List[int]) -> int:
        seen=set(arr)
        count=0
        for i in range(len(arr)):
            if arr[i]+1 in seen:
                count+=1
        return count
        