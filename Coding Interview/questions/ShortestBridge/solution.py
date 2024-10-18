from collections import deque

def shortest_bridge(grid):
    n = len(grid)
    
    def flood_fill(i, j):
      if i < 0 or i == n or j <0 or j == n: return
      if grid[i][j] == 0: return 
      if grid[i][j] == 2: return 
    
      grid[i][j] = 2
      flood_fill(i-1, j)
      flood_fill(i+1, j)
      flood_fill(i, j-1)
      flood_fill(i, j+1)
    
    loop_done = False
    for i in range(n):
      for j in range(n):
        if grid[i][j] == 0: continue
        flood_fill(i, j)
        loop_done = True
        break 
      if loop_done: break
    
    dq = deque()
    for i in range(n):
      for j in range(n):
        if grid[i][j] == 1: 
          dq.append([i+1,j, 1])
          dq.append([i-1,j, 1])
          dq.append([i,j+1, 1])
          dq.append([i,j-1, 1])
          
    while dq:
      i, j, d = dq.popleft()
      if (i<0) or (i==n) or (j<0) or (j ==n): continue
      if grid[i][j] == 2: 
        return d-1 
      if grid[i][j] == 1: continue
      grid[i][j] = 1
      dq.append([i+1, j, d+1])
      dq.append([i-1, j, d+1])
      dq.append([i, j+1, d+1])
      dq.append([i, j-1, d+1])
    return -1
