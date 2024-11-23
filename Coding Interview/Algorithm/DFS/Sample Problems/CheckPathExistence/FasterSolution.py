from collections import defaultdict

class Solution:
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination: return True
        
        visited = set()  
        adj = defaultdict(lambda:[])
                     
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        def dfs(node):
            visited.add(node)
            for nxt in adj[node]:
                if nxt in visited: continue
                dfs(nxt)
                
        dfs(source)
        return destination in visited
