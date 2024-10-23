# This solution has a but and fails one test cases as we know of.

def largest_rectangle(heights):

  n = len(heights)
  if n == 0: return 0
  d = {}
  d[heights[0]] = 0
  max_area = 0
  for i in range(1, n):
    ch = heights[i]
    hs = i 
    to_del = []
    for eh, pos in d.items(): 
      if ch >= eh: continue
      hs = min(i, pos)
      max_area = max(max_area, eh * (i - pos))
      to_del.append(eh)
    for eh in to_del: del d[eh]
    if ch in d: continue 
    d[ch] = hs
  for h, pos in d.items():
    max_area = max(max_area, (n-pos) * h)
  return max_area
    
  
