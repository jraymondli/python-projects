from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(lambda:[])
        ticket_cnt = defaultdict(lambda:0)
        for src, dst in tickets:
            adj[src].append(dst)
            ticket_cnt[(src, dst)] += 1
            
            
        paths = []
        def dfs(node, path, visited):
            if len(path) == (len(tickets) + 1):
                paths.append(path.copy())
                return
            
            for nxt in adj[node]:
                if (node, nxt) in visited and visited[(node, nxt)] == ticket_cnt[(node, nxt)]:
                    continue
                visited[(node, nxt)] += 1
                path.append(nxt)
                dfs(nxt, path, visited)
                path.pop()
                visited[(node, nxt)] -= 1

        dfs('JFK', ['JFK'], defaultdict(lambda:0))
        print(paths)
        p = paths[0]
        for i in range(1, len(paths)):
            p2 = paths[i]
            if ' '.join(p2) < ' '.join(p):
                p = p2 
        return p
            
            
