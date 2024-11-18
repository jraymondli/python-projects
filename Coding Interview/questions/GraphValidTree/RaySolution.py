from collections import deque, defaultdict 

def valid_tree(n, edges):
  if n == 1: return True 
  
  groups = {}
  for a, b in edges:
    if a not in groups and b not in groups:
      groups[a] = set([a, b])
      groups[b] = groups[a]
      continue 
    if a not in groups: 
      groups[b].add(a)
      groups[a] = groups[b]
      continue
    if b not in groups:
      groups[a].add(b)
      groups[b] = groups[a]
      continue 
    if groups[a] == groups[b]:
      return False 
    for node in groups[a]:
      groups[b].add(node)
    for node in groups[a]:
      groups[node] = groups[b]
  ts = set()
  ns = set()
  for node, group in groups.items():
    ns.add(node)
    ts.add(tuple(sorted(list(group))))
  if len(ns) != n: return False
  if len(ts) != 1: return False 
  return True 
