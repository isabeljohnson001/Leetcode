# Last updated: 10/8/2025, 9:48:11 PM
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:

        available=[] # servers: weight,index
        unavailable=[] #available_at, weight, index
        res=[0]*len(tasks)
        available=[(server,i) for i,server in enumerate(servers)]
        heapq.heapify(available)
        t=0
        for i in range(len(tasks)):
            t=max(t,i)
            if len(available)==0:
                t=unavailable[0][0]
            while unavailable and t>=unavailable[0][0] :
                timefree,weight, index=heapq.heappop(unavailable)
                heapq.heappush(available,(weight,index))
            weight, index=heapq.heappop(available)
            heapq.heappush(unavailable,(t+tasks[i],weight,index))
            res[i]=index
        return res
                




        