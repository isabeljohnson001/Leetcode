from collections import Counter
import heapq
class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        counts=Counter(arr)
        target=len(arr)/2
        ans=set()
        #sorted_counts=sorted(counts.items(),key=lambda x:x[1],reverse=True)
        
        heap=[]
        for item,freq in counts.items():
            heapq.heappush(heap,[-freq,item])
        
        removed_count=0
        while heap:
            freq,num=heapq.heappop(heap)
            ans.add(num)
            removed_count+=(-1*freq)

            if removed_count>=len(arr)//2:
                break
        
        return len(ans)



        