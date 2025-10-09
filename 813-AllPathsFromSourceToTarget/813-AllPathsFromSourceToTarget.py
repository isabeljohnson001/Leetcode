# Last updated: 10/8/2025, 9:49:47 PM
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:


        target=len(graph)-1
        ans=[]

        def backtrack(curr_node, path):
            if curr_node==target:
                ans.append(path[:])
                return

            for next_node in graph[curr_node]:
                path.append(next_node)
                backtrack(next_node,path)
                path.pop()
            
        path=[0]
        backtrack(0,path)

        return ans
        