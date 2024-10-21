# Observations: we can get max of the array to be a starting point and use two pointers i, j
# 1. meaningful starting point, i, woulb be a positive number
# 2. at the point the partial sum is <= 0, we need to move i to j + 1

def max_sub_array(nums):
  n = len(nums)
  i, j = 0, 0
  r = max(nums)
  s = 0
  while i < n and j < n: 
    if nums[i] <= 0:
      i += 1
      continue 
    if s == 0:
      s = nums[i]
      j = i + 1
      r = max(s, r)
      continue
    s += nums[j]
    r = max(s, r)
    j += 1
    if s <= 0:
      i = j 
      s = 0
  if s == 0: return r 
  return max(s, r)
      
    
    
