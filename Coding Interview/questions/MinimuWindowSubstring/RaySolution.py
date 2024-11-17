from collections import defaultdict

def contains(ds, dt):
  for key, freq in dt.items():
    if ds[key] < freq: return False 
  return True
  
def min_window(s, t):
    ns = len(s)
    min_window = ns + 1
    
    ds = defaultdict(lambda:0)
    dt = defaultdict(lambda:0)
    for c in t: dt[c] += 1
    
    ws, we = 0, 0 
    ms, me = 0, ns 
    
    while ws < ns and we <= ns:
      
      if not contains(ds, dt):
        if we <ns: ds[s[we]] += 1
        we += 1  
        continue 
      if (we-ws) < min_window:
        min_window = we - ws 
        ms, me = ws, we 
      ds[ s[ws] ] -= 1 
      ws += 1
      
    if min_window == (ns + 1): return ""
     
    return s[ms:me]

