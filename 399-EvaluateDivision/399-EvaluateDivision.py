# Last updated: 10/8/2025, 9:50:52 PM
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        def ans_query(start,end):
            if start not in graph:
                return -1
            
            seen=set()
            seen.add(start)
            stack=[(start,1)]

            while stack:
                node,ratio=stack.pop()
                if node==end:
                    return ratio
                for neigbour in graph[node]:
                    if neigbour not in seen:
                        seen.add(neigbour)
                        stack.append((neigbour,ratio*graph[node][neigbour]))
            return -1
        


        graph=defaultdict(dict)
        for i in range(len(equations)):
            numerator,denominator=equations[i]
            value=values[i]
            graph[numerator][denominator]=value
            graph[denominator][numerator]=1/value

        ans=[]
        for i in range(len(queries)):
            numerator,denominator=queries[i]
            ans.append(ans_query(numerator,denominator))
        return ans
            