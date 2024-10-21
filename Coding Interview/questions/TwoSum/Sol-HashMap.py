from collections import defaultdict
def two_sum(arr, t):
    
    v_dict = defaultdict(lambda:[])
    for i, val in enumerate(arr):
      v_dict[val].append(i)
      
    for i, val in enumerate(arr):
      if (t-val) not in v_dict: continue
      if val != (t-val): return [i, v_dict[t-val][0]]
      if len(v_dict[val]) < 2: continue 
      return v_dict[val][:2]

    return []
    
