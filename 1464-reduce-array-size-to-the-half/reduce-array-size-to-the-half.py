from collections import Counter
import heapq
class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        counts=Counter(arr)
        target=len(arr)/2
        ans=set()
        sorted_counts=sorted(counts.items(),key=lambda x:x[1],reverse=True)
        removed_count=0
        
        for num, freq in sorted_counts:
            ans.add(num)
            removed_count+=freq

            if removed_count>=len(arr)//2:
                break
        
        
        
        return len(ans)



        