import math
from collections import defaultdict 
from heapq import heappush, heappop

def network_delay_time(times, n, k):

  latency_dict = {}
  neighbors = defaultdict(lambda:[])
  for x, y, t in times:
    neighbors[x].append(y)
    latency_dict[(x,y)] = t 
    
  visited = set()
  pq =[[0, k]]
  distances = [math.inf] * (n + 1)
  distances[k] = 0
  while pq: 
    l, node = heappop(pq)
    if node in visited: continue
    visited.add(node)
    for nxt in neighbors[node]:
      if distances[nxt] > (distances[node] + latency_dict[(node, nxt)]):
        distances[nxt] = distances[node] + latency_dict[(node, nxt)]
        heappush(pq, [distances[nxt], nxt])
  latency = max(distances[1:])

  if latency == math.inf: return -1
  return latency 
    
