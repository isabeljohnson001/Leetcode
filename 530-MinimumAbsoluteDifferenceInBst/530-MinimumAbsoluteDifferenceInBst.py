# Last updated: 10/8/2025, 9:50:41 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node):

            if not node:
                return
            left=dfs(node.left)
            values.append(node.val)
            right=dfs(node.right)

        values=[]
        dfs(root)
        ans=float("inf")
        for i in range(1,len(values)):
            ans=min(ans,values[i]-values[i-1])
        return ans



        