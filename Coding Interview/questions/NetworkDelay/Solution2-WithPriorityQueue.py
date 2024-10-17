import math
from collections import defaultdict 
from heapq import heappush, heappop

def network_delay_time(times, n, k):

  neighbors = defaultdict(lambda:[])
  for x, y, t in times:
    neighbors[x].append([y, t])
    
  visited = set()
  pq =[[0, k]]
  distances = [math.inf] * (n + 1)
  distances[k] = 0
  while pq: 
    l, node = heappop(pq)
    if node in visited: continue
    visited.add(node)
    for nxt, t in neighbors[node]:
      if distances[nxt] > (distances[node] + t):
        distances[nxt] = distances[node] + t
        heappush(pq, [distances[nxt], nxt])
        
  latency = max(distances[1:])
  return latency if latency != math.inf else -1
    
