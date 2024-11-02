def rob_houses(nums):

  n = len(nums)
  if n <= 2: return max(nums)
  
  prev2 = nums[0]
  prev1 = max(nums[:2])
  
  for i in range(2, n):
    curr = max(prev1, prev2 + nums[i])
    prev2 = prev1 
    prev1 = curr 
    
  return curr
