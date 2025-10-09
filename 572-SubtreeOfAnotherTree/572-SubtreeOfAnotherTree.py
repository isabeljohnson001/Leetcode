# Last updated: 10/8/2025, 9:50:34 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def isSame(p,q):
            if p==None and q==None:
                return True
            if p==None or q==None:
                return False
            if p.val!=q.val:
                return False
            left=isSame(p.left,q.left)
            right=isSame(p.right,q.right)
            return left and right
        def dfs(node):
            if not node:
                return False
            elif isSame(node,subRoot):
                return True
            else:
                return dfs(node.left) or dfs(node.right)

        return dfs(root)            