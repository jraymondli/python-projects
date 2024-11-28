def kth_lucky_number(k):
  
    d, num = 1, k 
    num -= 1 
    while num >= (1 << d): 
      num -= 1 << d
      d += 1 
    
    r = ""
    for i in range(d-1, -1, -1):
      if num & (1 << i): r += '7'
      else: r += '4'
    return r 
    
 
