class UnionFind:

    # Constructor
    def __init__(self, n):
        self.parents = []
        for i in range(n):
            self.parents.append(i)

    # Function to find which subset a particular element belongs to
    def find(self, v):
        if self.parents[v] != v:
            return self.find(self.parents[v])
        return v
   
    # Function to join two subsets into a single subset
    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        self.parents[p1] = p2
