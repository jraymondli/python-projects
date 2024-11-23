"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None: return None

        visited = set()
        mapping = {}
        def dfs(n):
            visited.add(n)
            new_node = Node(n.val)
            mapping[n] = new_node
            for nxt in n.neighbors:
                if nxt in visited: continue 
                dfs(nxt)
        dfs(node)

        for n, new_node in mapping.items():
            for nxt in n.neighbors:
                new_node.neighbors.append(mapping[nxt])

        return mapping[node]
