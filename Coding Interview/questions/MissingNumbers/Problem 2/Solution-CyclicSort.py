from traversal import *

def find_missing_number(nums):
  
  n = len(nums)
  for i in range(n):
    while nums[i] not in [i, n]:
      j = nums[i]
      nums[i], nums[j] = nums[j], nums[i]
      
  for i in range(n):
    if i != nums[i]: return i
  
  return n
    
  
