from collections import defaultdict 
from collections import deque

def loud_and_rich(richer, quiet):
    n = len(quiet)
    res = list(range(n))
    
    adj = defaultdict(lambda:[])
    adjr = defaultdict(lambda:[])
    for a, b in richer:
      adj[b].append(a)
      adjr[a].append(b)
        
    dq, d_resolved = deque(), {}
    for i in range(n):
      d_resolved[i] = len(adj[i])
      if d_resolved[i] == 0:
        dq.append(i)
          
    while dq:
      i = dq.popleft()
      for nxt in adj[i]:
        if quiet[res[nxt]] < quiet[res[i]]: res[i] = res[nxt]
      for nxt in adjr[i]:
        d_resolved[nxt] -= 1
        if d_resolved[nxt] == 0: dq.append(nxt)
    return res 
