import math
from collections import defaultdict 
from heapq import heappush, heappop

def network_delay_time(times, n, k):

    visited = set()
    adj_dict = defaultdict(lambda:[])
    for s, e, d in times:
      adj_dict[s].append([e, d])
    distance = [math.inf] * (n+1)
    distance[k] = 0
    dq = [[0, k]]
    
    while len(visited)< n and dq:
      min_d, min_n = heappop(dq)
      visited.add(min_n)
      for nb, d in adj_dict[min_n]:
        if distance[nb] > (distance[min_n] + d):
          distance[nb] = distance[min_n] + d
          heappush(dq, [distance[nb], nb])
 
    rv = max(distance[1:])
    if rv == math.inf: rv = -1
    return rv 
