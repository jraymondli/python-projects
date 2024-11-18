from collections import deque, defaultdict 

def shareStation(bus_routes, i, j):
  for s in bus_routes[i]:
    if s in bus_routes[j]:
      return True 
  return False 
  
def minimum_buses(bus_routes, src, dest):
    if src == dest: return 0
    
    adj = defaultdict(lambda:[])
    n_buses = len(bus_routes) 
    for i in range(n_buses):
      for j in range(i+1, n_buses):
        if shareStation(bus_routes, i, j):
          adj[i].append(j)
          adj[j].append(i)
          
    visited = [False]*n_buses
    dq = deque()
    targets = set()
    for i, bus in enumerate(bus_routes):
      if src in bus: dq.append([1, i])
      if dest in bus: targets.add(i)
    while dq:
      s, b = dq.popleft() 
      if b in targets: return s
      visited[b] = True 
      for nxt in adj[b]:
        if visited[nxt]: continue
        dq.append([s+1, nxt])
    return -1
