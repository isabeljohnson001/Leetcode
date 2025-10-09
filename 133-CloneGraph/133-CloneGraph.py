# Last updated: 10/8/2025, 9:52:14 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        hashMap={}
        def dfs(curr_node):
            if curr_node in hashMap:
                return hashMap[curr_node]

            clone=Node(curr_node.val)
            hashMap[curr_node]=clone
            for nei in curr_node.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone
        
        return dfs(node)