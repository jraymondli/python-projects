def remove_stones(stones):
  
  
  ns = len(stones)
  edges = []
  for i in range(ns):
    for j in range(i+1, ns):
      if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
        edges.append([i, j])
        
  grp_dict = {i: set([i]) for i in range(ns)}
  
  for a, b in edges:
    if grp_dict[a] == grp_dict[b]: continue
    for c in grp_dict[b]: grp_dict[a].add(c)
    for c in grp_dict[b]: grp_dict[c] = grp_dict[a]
    
  grps = set()
  for _, grp in grp_dict.items():
    grps.add(tuple(grp))
  
  return ns - len(grps)
    
