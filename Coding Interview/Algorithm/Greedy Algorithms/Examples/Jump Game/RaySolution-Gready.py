def jump_game(nums):
    
    n = len(nums)
    if n == 1: return True 

    last_index = n - 1
    while last_index > -1:
      last_index_updated = False
      for i in range(last_index-1, -1, -1):
        if nums[i] >= (last_index - i):
          last_index = i 
          if i == 0: return True 
          last_index_updated = True
          break 
      if not last_index_updated: break 
    return False


## Time Complexity O(n) 
## Space Compaxity O(1)

