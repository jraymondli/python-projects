from collections import defaultdict 
from collections import deque

def loud_and_rich(richer, quiet):
    n = len(quiet)
    res = [0] * n 
    
    adj = defaultdict(lambda:[])
    adjr = defaultdict(lambda:[])
    d_resolved = {}
    for a, b in richer:
      adj[b].append(a)
      adjr[a].append(b)
    dq = deque()
    for i, depenencies in adj.items():
      d_resolved[i] = len(depenencies)
    for i in range(n):
      if i not in adj:
        dq.append(i)
    while dq:
      i = dq.popleft()
      qmin_i, qmin = i, quiet[i]
      for nxt in adj[i]:
        if quiet[res[nxt]] < quiet[qmin_i]:
          qmin_i, qmin = res[nxt], quiet[nxt]
      res[i] = qmin_i
      for nxt in adjr[i]:
        d_resolved[nxt] -= 1
        if d_resolved[nxt] == 0: dq.append(nxt)
    return res 
