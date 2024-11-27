def jump_game(nums):
    
    n = len(nums)
    if n == 1: return True 
    reached = [False] * n 
    reached[0] = True 
    
    for i in range(n):
      if not reached[i]: continue
      for j in range(1, nums[i]+1):
        nxt_index = i + j
        if nxt_index >= n: continue 
        if nxt_index == (n-1): return True 
        reached[nxt_index] = True 

    return False


# Complexity: 
#     - Time O(n^2)
#     - Space O(n)
