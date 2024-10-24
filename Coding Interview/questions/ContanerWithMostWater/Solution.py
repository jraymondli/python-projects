def container_with_most_water(height):

  n = len(height)
  
  l, r = 0, n-1 
  max_area = 0
  while l < r:
    max_area = max(max_area, (r-l) * min(height[l], height[r]))
    
    if height[l] < height[r]:
      l_updated = False
      for i in range(l+1, r):
        if height[i] <= height[l]: continue
        l = i 
        l_updated = True
        break 
      if not l_updated: break 
    else:
      r_updated = False
      for i in range(r-1, l, -1):
        if height[i] <= height[r]: continue
        r = i 
        r_updated = True
        break
      if not r_updated: break 
      
  return max_area
