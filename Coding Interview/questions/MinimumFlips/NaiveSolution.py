def min_flips(s):
    n = len(s)
    if n == 1: return 0 
    
    max_ops = n
    for i in range(n):
      ops1 = 0
      ops2 = 0
      for i in range(n):
        c = '1' if i % 2 == 1 else '0'
        if s[i] == c: ops1 += 1
        if s[i] != c: ops2 +=1 
      max_ops = min([max_ops, ops1, ops2])
      
      s = s[1:] + s[0]
      
    return max_ops
