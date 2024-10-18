from union_find import UnionFind

def count_components(n, edges):


    uf = UnionFind(n)
    for a, b in edges:
      uf.union(a, b)
      
    grp_s = set()
    for i in uf.parents:
      grp_s.add(uf.find(i))
    return len(grp_s)



