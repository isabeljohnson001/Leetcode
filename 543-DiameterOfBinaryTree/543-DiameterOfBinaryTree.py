# Last updated: 10/8/2025, 9:50:37 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        daimeter=0

        def longestPath(node):
            if not node:
                return 0
            nonlocal daimeter
            left=longestPath(node.left)
            right=longestPath(node.right)
            daimeter=max(daimeter,left+right)

            return max(left,right)+1
        longestPath(root)
        return daimeter