def largest_rectangle(heights):

  n = len(heights)
  if n == 0: return 0
  d = {}
  d[heights[0]] = 0
  max_area = 0
  for i in range(1, n):
    ch = heights[i]
    hs = i
    if ch in d: hs = d[ch]
    to_del = []
    for eh, pos in d.items(): 
      if ch >= eh: continue
      hs = min(hs, pos)
      max_area = max(max_area, eh * (i - pos))
      to_del.append(eh)
    for eh in to_del: del d[eh]
    if ch in d: continue 
    d[ch] = hs
  for h, pos in d.items():
    max_area = max(max_area, (n-pos) * h)
  return max_area


# The bug has been fixed here with the key change on line 15

    
  
