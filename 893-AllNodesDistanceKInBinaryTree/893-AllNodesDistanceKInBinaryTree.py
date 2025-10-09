# Last updated: 10/8/2025, 9:49:45 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        graph=defaultdict(list)
        ans=[]
        def build_graph(cur,parent):
            if cur and parent:
                graph[parent.val].append(cur.val)
                graph[cur.val].append(parent.val)
            if cur.left:
                build_graph(cur.left,cur)
            if cur.right:
                build_graph(cur.right,cur)

        def dfs(node,distance):
            if distance == k:
                ans.append(node)
                return
            for neighbour in graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    dfs(neighbour,distance+1)


        build_graph(root,None)
        seen={(target.val)}
        dfs(target.val,0)
        return ans

        