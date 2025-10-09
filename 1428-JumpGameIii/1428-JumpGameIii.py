# Last updated: 10/8/2025, 9:49:05 PM
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:


        queue=collections.deque()
        queue.append(start)
        n=len(arr)
        while queue:

            node=queue.popleft()
            if arr[node]==0:
                return True
            if arr[node]<0:
                continue

            for i in [node-arr[node],node+arr[node]]:
                if 0<=i<n:
                    queue.append(i)
            arr[node]=-arr[node]
        
        return False