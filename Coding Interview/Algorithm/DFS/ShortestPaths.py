from collections import defaultdict
import math
visited = set()
paths=[]
def dfs(n, target, path):

    for nxt in adj[n]:
        if nxt in path: continue 
        path.append(nxt)
        if nxt == target:
            paths.append(path.copy())
        else:
            dfs(nxt, target, path)
        path.pop()

edges = [['a', 'b'], ['a', 'c'], ['a', 'd'], ['d', 'e'], ['e', 'f'], ['b', 'e'], ['b', 'f'], ['c', 'e']]
adj = defaultdict(lambda:[])
for a,b in edges:
    adj[a].append(b)
    adj[b].append(a)

dfs('a', 'b', ['a'])
min_len, min_p = math.inf, None
for p in paths:
    if len(p) < min_len:
        min_p = p 
        min_len = len(p)

print(min_p)
