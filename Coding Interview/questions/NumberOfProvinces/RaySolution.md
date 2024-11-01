# Using DFS

from collections import defaultdict

def find_connected_cities(cities):
  
    n = len(cities)
    adj = defaultdict(lambda:[])
    
    for i in range(n):
      for j in range(i+1, n):
        if cities[i][j] == 1:
          adj[i].append(j)
          adj[j].append(i)
          
    visited = [False] * n 
    n_provinces = 0
    
    def dfs(nd):
      visited[nd] = True 
      for nxt in adj[nd]:
        if not visited[nxt]:
          dfs(nxt)
          
    for i in range(n):
      if visited[i]: continue
      n_provinces += 1
      dfs(i)
    return n_provinces


      
