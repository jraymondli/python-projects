from union_find import *

def remove_stones(stones):
 
  OFFSET = 100
  uf = UnionFind()
  for x, y in stones:
    uf.union(x, y + OFFSET)
  groups = set()
  for i in uf.parents:
    groups.add(uf.find(i))
    
  return len(stones) - len(groups)
