# Last updated: 10/8/2025, 9:48:02 PM
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        #iterate through each bomb and create an adjusceny list
        adj=collections.defaultdict(list)

        for i in range(len(bombs)):
            for j in range(i+1,len(bombs)):

                x1,y1,r1=bombs[i]
                x2,y2,r2=bombs[j]
                
                d=sqrt((x1-x2)**2+(y1-y2)**2)
                if d<=r1:
                    adj[i].append(j)
                if d<=r2:
                    adj[j].append(i)
                    
        #then define dfs
        def dfs(i,visit):
            if i in visit:
                return 0
            visit.add(i)
            for neigbour in adj[i]:
                dfs(neigbour,visit)
            return len(visit)
            



        #call the main functions, call the main function..pass each bomb to dfs..find the no of bombs that canbe blasted by vurrent bomb..return the max
        res=0
        for i in range(len(bombs)):
            res=max(dfs(i,set()),res)
        return res
        