class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph)
        paths = []

        def dfs(i, p):
            if i == (n-1):
                paths.append(p.copy())

            for nxt in graph[i]:
                p.append(nxt)
                dfs(nxt, p)
                p.pop()

        dfs(0, [0])
        return paths
