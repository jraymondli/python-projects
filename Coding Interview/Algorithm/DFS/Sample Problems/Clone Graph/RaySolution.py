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

        dic = {}
        dic_n = {}

        visited = set()
        dq = deque()

        dq.append(node)
        visited.add(node.val)

        while(dq):
            nd = dq.popleft()
            dic[nd.val] = nd
            dic_n[nd.val] = Node(nd.val)
            for nb in nd.neighbors:
                if nb.val in visited: continue
                dq.append(nb)
                visited.add(nb.val)

        for val, nd in dic.items():
            new_nd = dic_n[val]
            for nb in nd.neighbors:
                new_nd.neighbors.append(dic_n[nb.val])

        return dic_n[node.val]
