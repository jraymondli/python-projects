from collections import deque 

def min_k_bit_flips( nums, k):
        
    n = len(nums)
    dq = deque() 
    flip_count = 0
    
    for i in range(n-k+1):
      while dq and dq[0] <= (i - k):
        dq.popleft()
      if (nums[i] + len(dq)) % 2: continue
      dq.append(i)
      flip_count += 1 
    for i in range(n-k+1, n):
      while dq and dq[0] <= (i - k):
        dq.popleft()
      if (nums[i] + len(dq)) % 2: continue
      return -1 
    return flip_count 
      
    
        
