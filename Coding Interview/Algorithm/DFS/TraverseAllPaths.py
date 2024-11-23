from collections import defaultdict

visited = set()
def dfs(n, target, path):

    for nxt in adj[n]:
        if nxt in path: continue 
        path.append(nxt)
        if nxt == target:
            print(path)
        else:
            dfs(nxt, target, path)
        path.pop()

edges = [['a', 'b'], ['a', 'c'], ['a', 'd'], ['d', 'e'], ['e', 'f'], ['b', 'e'], ['b', 'f'], ['c', 'e']]
adj = defaultdict(lambda:[])
for a,b in edges:
    adj[a].append(b)
    adj[b].append(a)

print(adj)

dfs('a', 'b', ['a'])
