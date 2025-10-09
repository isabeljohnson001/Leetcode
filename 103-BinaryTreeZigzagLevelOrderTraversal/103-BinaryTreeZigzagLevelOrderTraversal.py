# Last updated: 10/8/2025, 9:52:29 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res=[]
        
        q=deque([root] if root else [])
        
        while q:
            curr_len=len(q)
            level=[]

            for _ in range(curr_len):
                
                node=q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
            level=list(reversed(level)) if len(res)%2 else level
            res.append(level)
        return res
        