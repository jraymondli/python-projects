def smallest_missing_positive_integer(nums):

  n = len(nums)
  for i in range(n):
    while nums[i] != (i+1) and nums[i] > 0 and nums[i] <=n: 
      j = nums[i] - 1 
      if nums[i] == nums[j]: break
      nums[i], nums[j] = nums[j], nums[i]
      
  for i in range(n):
    if nums[i] != (i+1): return i + 1 
    
  return n +1 
