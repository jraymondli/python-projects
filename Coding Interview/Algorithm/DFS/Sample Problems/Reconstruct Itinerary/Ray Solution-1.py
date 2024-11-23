from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(lambda:[])
        for src, dst in tickets:
            adj[src].append(dst)
            
        paths = []
        def dfs(node, path, visited):
            if len(visited) == len(tickets):
                paths.append(path.copy())
                return
            
            for nxt in adj[node]:
                if (node, nxt) in visited: continue
                visited.add((node, nxt))
                path.append(nxt)
                dfs(nxt, path, visited)
                path.pop()
                visited.remove((node, nxt))

        dfs('JFK', ['JFK'], set())
        print(paths)
        p = paths[0]
        for i in range(1, len(paths)):
            p2 = paths[i]
            if ' '.join(p2) < ' '.join(p):
                p = p2 
        return p
