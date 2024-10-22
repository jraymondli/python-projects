from collections import deque

def remove_min_intervals(intervals):

    n = len(intervals)
    intervals.sort()
    
    dq = deque()
    
    if n <=1: return 0 
    dq.append(intervals[0])
    for j in range(1, n):
      i1 = dq[-1]
      i2 = intervals[j]
      if i2[0] >= i1[1]: 
        dq.append(i2)
        continue
      if i2[1] >= i1[1]: continue 
      dq.pop() 
      dq.append(i2)
    return n - len(dq)
    
