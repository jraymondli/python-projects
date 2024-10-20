# avoid duplicating code
from collections import deque

def initGrid(m, n):
  grid = []
  for i in range(m): 
    row = [0]*n 
    grid.append(row)
  return grid 

def getFlowGrid(heights, m, n, to_pacific=True):
  flowGrid = initGrid(m, n)
  dq = deque()
  for i in range(m):
    if to_pacific: dq.append([i, 0])
    else: dq.append([i, n-1])
  for j in range(n):
    if to_pacific: dq.append([0, j])
    else: dq.append([m-1, j])
    
  while dq: 
      r, c = dq.popleft() 
      if flowGrid[r][c] == 1: continue 
      flowGrid[r][c] = 1
      if r < (m-1) and heights[r+1][c] >= heights[r][c]:
        dq.append([r+1, c])
      if r>0 and heights[r-1][c]>= heights[r][c]:
        dq.append([r-1, c])
      if c < (n-1) and heights[r][c+1] >= heights[r][c]:
        dq.append([r, c+1])
      if c > 0 and heights[r][c-1] >= heights[r][c]:
        dq.append([r, c-1])  
  return flowGrid
      
def estimate_water_flow(heights):
    m, n = len(heights), len(heights[0])
    
    pacific_grid = getFlowGrid(heights, m, n, to_pacific=True)
    atlantic_grid = getFlowGrid(heights, m, n, to_pacific=False)
        
    results = [] 
    for i in range(m):
      for j in range(n):
        if pacific_grid[i][j] == 1 and atlantic_grid[i][j] == 1:
          results.append([i, j])
    return results
