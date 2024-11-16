def min_window(str1, str2):
    
    
  
    l1, l2 = len(str1), len(str2)
    ms, me = 0, l1+1
  
    for ws in range(l1) :
      if str2[0] != str1[ws]: continue 
      we = ws +1
      match_next = 1 
      while we < l1 and match_next < l2: 
        if str1[we] == str2[match_next]:
          match_next += 1 
        we += 1
      print(match_next, l2)
      if match_next == l2:
        if (we - ws) < (me - ms):
          me, ms = we, ws
    
    if me == (l1+1): return ""
    return str1[ms: me]
