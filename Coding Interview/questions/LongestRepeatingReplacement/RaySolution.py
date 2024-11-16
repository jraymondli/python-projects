from collections import defaultdict

def longest_repeating_character_replacement(s, k):    
  max_len = k 
  ns = len(s)
  
  for i in range(ns):
    d = defaultdict(lambda:0)
    max_c = 0
    hit_max = False
    for j in range(i,ns):
      c = s[j]
      d[c] += 1
      max_c = max(max_c, d[c])
      total_c = j - i + 1 
      if (total_c - max_c) > k: 
        max_len = max(max_len, j-i)
        hit_max = True
        break 
    if not hit_max: 
      max_len = max(max_len, ns-i)
    
  return max_len
        
  
    
