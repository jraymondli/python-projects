# This exceeds time on case 12

from collections import defaultdict

class Solution:
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination: return True
        
        adj = defaultdict(lambda:[])
        def dfs(node, destination, path, visited, result):
            for nxt in adj[node]:
                if nxt in visited: continue
                path.append(nxt)
                visited.add(nxt)
                if nxt == destination:
                    result.append(path.copy())
                else:
                    dfs(nxt, destination, path, visited, result)
                path.pop() 
                visited.remove(nxt)
                
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        result, visited = [], set()
        dfs(source, destination, [source], visited, result)
        return len(result) != 0
