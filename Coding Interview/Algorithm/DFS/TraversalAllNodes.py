from collections import defaultdict

visited = set()
def dfs(n):
    print(n)
    visited.add(n)
    for nxt in adj[n]:
        if nxt in visited: continue 
        dfs(nxt)

edges = [['a', 'b'], ['a', 'c'], ['a', 'd'], ['d', 'e'], ['e', 'f'], ['b', 'f']]
adj = defaultdict(lambda:[])
for a,b in edges:
    adj[a].append(b)
    adj[b].append(a)

dfs('a')
