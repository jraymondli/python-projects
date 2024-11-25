from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph)
        dq = deque([[0]])
        paths = []
        while dq:
            p = dq.popleft()
            node = p[-1]
            for nxt in graph[node]:
                if nxt in p: continue
                new_p = p.copy()
                new_p.append(nxt)
                if nxt == (n-1):
                    paths.append(new_p)
                else:
                    dq.append(new_p)

        return paths

