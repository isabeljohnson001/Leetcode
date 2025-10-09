# Last updated: 10/8/2025, 9:51:54 PM
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap={i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        output=[]
        # courses can have different states here:
        '''
        1.visited=the course is already visited and added to output.
        2.course is visiting along the path, but added to cycle
        3. course is not yet visited.

        '''
        visit=set()
        cycle=set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []
        return output