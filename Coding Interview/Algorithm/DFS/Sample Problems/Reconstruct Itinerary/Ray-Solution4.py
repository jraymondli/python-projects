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
            
        def dfs(node, path, visited):
            if len(path) == (len(tickets) + 1):
                return path
            
            for nxt in adj[node]:
                if (node, nxt) in visited and visited[(node, nxt)] == ticket_cnt[(node, nxt)]:
                    continue
                visited[(node, nxt)] += 1
                path.append(nxt)
                pr = dfs(nxt, path, visited)
                if pr: return pr
                path.pop()
                visited[(node, nxt)] -= 1
            return []

        return dfs('JFK', ['JFK'], defaultdict(lambda:0))
