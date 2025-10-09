# Last updated: 10/8/2025, 9:50:44 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue=deque([root])
        ans=[]

        while queue:

            current_level=len(queue)
            currMax=float("-inf")
            for i in range(current_level):
                node=queue.popleft()
                currMax=max(currMax,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(currMax)
        return ans




        