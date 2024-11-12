from collections import defaultdict

def count_components(n, edges):

  neighbors = defaultdict(lambda:[])
  for a,b in edges:
    neighbors[a].append(b)
    neighbors[b].append(a)
  visited = [False] * n 
  
  def dfs(i):
    visited[i] = True 
    for nxt in neighbors[i]:
      if not visited[nxt]: dfs(nxt)
      
  count = 0 
  for i in range(n):
    if visited[i]: continue
    dfs(i)
    count += 1
  return count 
