# Last updated: 10/8/2025, 9:49:16 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        curr_sum=0
        
        q=deque([root] if root else [])
        
        
        while(q):
            
            curr_len=len(q)
            curr_sum=0
            for _ in range(curr_len):
                
                node=q.popleft()
                curr_sum+=node.val
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
        return curr_sum
        
            

