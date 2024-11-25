from collections import defaultdict

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        adj = defaultdict(lambda:[])
        for a, b in edges:
            adj[a].append(b)

        visited = set()
        nodes_to_destination = set()
        def dfs(node, path):
            visited.add(node)
            if adj[node] == []:
                if node != destination: 
                    return False
                else:
                    for nd in path: nodes_to_destination.add(nd)
                    return True
            for nxt in adj[node]:
                if nxt in visited and nxt not in nodes_to_destination: 
                    return False
                path.append(nxt)
                sv = dfs(nxt, path)
                path.pop()
                if not sv: 
                    return False
            return True

        return dfs(source, [])
