from collections import deque

def initGrid(m, n):
  grid = []
  for i in range(m): 
    row = [0]*n 
    grid.append(row)
  return grid 
  
def estimate_water_flow(heights):
    m = len(heights)
    n = len(heights[0])
    
    to_pacific = initGrid(m, n)
    dq = deque()
    for i in range(m):
      dq.append([i, 0])
    for j in range(n):
      dq.append([0, j])
    while dq: 
      r, c = dq.popleft() 
      if to_pacific[r][c] == 1: continue 
      to_pacific[r][c] = 1
      if r < (m-1) and heights[r+1][c] >= heights[r][c]:
        dq.append([r+1, c])
      if r>0 and heights[r-1][c]>= heights[r][c]:
        dq.append([r-1, c])
      if c < (n-1) and heights[r][c+1] >= heights[r][c]:
        dq.append([r, c+1])
      if c > 0 and heights[r][c-1] >= heights[r][c]:
        dq.append([r, c-1])
    
    to_atlantic = initGrid(m, n)
    dq = deque()
    for i in range(m):
      dq.append([i, n-1])
    for j in range(n):
      dq.append([m-1, j])
    while dq: 
      r, c = dq.popleft() 
      if to_atlantic[r][c] == 1: continue 
      to_atlantic[r][c] = 1
      if r < (m-1) and heights[r+1][c] >= heights[r][c]:
        dq.append([r+1, c])
      if r>0 and heights[r-1][c]>= heights[r][c]:
        dq.append([r-1, c])
      if c < (n-1) and heights[r][c+1] >= heights[r][c]:
        dq.append([r, c+1])
      if c > 0 and heights[r][c-1] >= heights[r][c]:
        dq.append([r, c-1])
        
    results = [] 
    for i in range(m):
      for j in range(n):
        if to_pacific[i][j] == 1 and to_atlantic[i][j] == 1:
          results.append([i, j])
    return results
