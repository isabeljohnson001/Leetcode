# Last updated: 10/8/2025, 9:52:28 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        else: 
            left=self.maxDepth(root.left)
            right=self.maxDepth(root.right)

            return max(left,right)+1
        #left=self.maxDepth(root.left)
        #right=self.maxDepth(root.right)
        
        #return max(right,left)+1


#if using bfs
        #level=0
        #q=deque([root])
        #while q:
        #    for i in range(len(q)):
        #        node=q.popleft()
        #        if node.left:
        #            q.append(node.left)
        #        if node.right:
        #            q.append(node.right)
        #    level+=1
        #return level


        #usibg DFS stack
        '''
        res=0
        stack=[[root,1]]
        while stack:
            node,depth=stack.pop()
            if node:
                res=max(res,depth)
                stack.append([node.left,depth+1])
                stack.append([node.right,depth+1])
        return res
        '''

        



