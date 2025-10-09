# Last updated: 10/8/2025, 9:49:01 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node,maxSoFar):
            ans=0
            if not node:
                return 0

            left=dfs(node.left,max(maxSoFar,node.val))
            right=dfs(node.right,max(maxSoFar,node.val))
            ans=left+right

            if node.val>=maxSoFar:
                ans+=1
            return ans
        return dfs(root,float("-inf"))


        