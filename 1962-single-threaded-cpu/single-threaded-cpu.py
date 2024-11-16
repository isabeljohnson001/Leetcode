class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res=[]
        minHeap=[]
        t=0
        for i,t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda x:x[0])
        print(tasks)
        #At t=0 1,2
        i,t=0,tasks[0][0]    
        while minHeap or i<len(tasks):
            while  i<len(tasks) and tasks[i][0]<=t:
                heapq.heappush(minHeap,[tasks[i][1],tasks[i][2]])
                i+=1
            if not minHeap:
                t=tasks[i][0]
            else:
                proc_time,index=heapq.heappop(minHeap)
                t+=proc_time
                res.append(index)
        return res

        