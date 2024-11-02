def min_flips(s):

    n = len(s)
  
    alt1 = ''.join(['1' if i %2 == 1 else '0' for i in range(2*n)])
    alt2 = ''.join(['0' if i %2 == 1 else '1' for i in range(2*n)])
    
    s = s * 2 
    min_flips = n 
    
    diff1 = sum([1 if alt1[i] != s[i] else 0 for i in range(n)])
    diff2 = sum([1 if alt2[i] != s[i] else 0 for i in range(n)])
    
    for i in range(n):
      min_flips = min([min_flips, diff1, diff2])
      
      if alt1[i] != s[i]: diff1 -= 1 
      if alt1[i+n] != s[i+n]: diff1 += 1 
      
      if alt2[i] != s[i]: diff2 -= 1 
      if alt2[i+n] != s[i+n]: diff2 += 1 
    
    return min_flips
