def find_corrupt_pair(nums):

    n = len(nums)
    for i in range(n):
      
      while nums[i] != (i+1):
        j = nums[i] -1 
        if nums[i] == nums[j]: break
        nums[i], nums[j] = nums[j], nums[i]
        
    for i in range(n):
      if nums[i] != (i + 1):
        return [i+1, nums[i]]
        
      
