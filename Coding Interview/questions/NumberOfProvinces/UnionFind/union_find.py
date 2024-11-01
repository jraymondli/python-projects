class UnionFind:
      def __init__(self, n):
          self.root = [i for i in range(n)]
          self.rank = [0] * n
          self.count = n
      
      def find(self, x):
          if x != self.root[x]:
              self.root[x] = self.find(self.root[x])
          
          return self.root[x]
      
      def union(self, x, y):
          root_x, root_y = self.find(x), self.find(y)

          if root_x == root_y:
              return
          
          if self.rank[root_x] > self.rank[root_y]:
              self.root[root_y] = root_x
          elif self.rank[root_x] < self.rank[root_y]:
              self.root[root_x] = root_y
          else:
              self.root[root_y] = root_x
              self.rank[root_x] += 1
          
          self.count -= 1
