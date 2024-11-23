# This fails on test case 80

from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(lambda:[])
        ticket_cnt = defaultdict(lambda:0)
        for src, dst in tickets:
            adj[src].append(dst)
            ticket_cnt[(src, dst)] += 1
        for _, nxt_list in adj.items():
            nxt_list.sort()
            
        paths = []
        def dfs(node, path, visited):
            if len(path) == (len(tickets) + 1):
                paths.append(path.copy())
                return True
            
            for nxt in adj[node]:
                if (node, nxt) in visited and visited[(node, nxt)] == ticket_cnt[(node, nxt)]:
                    continue
                visited[(node, nxt)] += 1
                path.append(nxt)
                if dfs(nxt, path, visited): return True
                path.pop()
                visited[(node, nxt)] -= 1
            return False

        dfs('JFK', ['JFK'], defaultdict(lambda:0))
        return paths[0]
            
            
