# Last updated: 10/8/2025, 9:52:30 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res=[]
        queue=deque([root])

        while queue:
            current_level=len(queue)
            path=[]
            for i in range(current_level):
                node=queue.popleft()
                path.append(int(node.val))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(path)
        return res

                    



        
        