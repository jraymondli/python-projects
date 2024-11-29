def find_longest_substring(s):

    ns = len(s)
    if ns == 1: return 0 if s[0] in ['a', 'e', 'i', 'o', 'u'] else 1
    
    max_len = 0
    
    masks = { 'a': 1, 'e':2, 'i': 4, 'o':8, 'u': 16}
    val_array = []
    val = 0
    val_array.append(val)
    for c in s: 
      m = masks.get(c, 0)
      val = val ^ m
      val_array.append(val)
      
    val_dict = {}
    for i in range(ns+1):
      val = val_array[i]
      if val not in val_dict: 
        val_dict[val] = i 
      else:
        l = i - val_dict[val]
        max_len = max (max_len, l)
        
  
    return max_len
