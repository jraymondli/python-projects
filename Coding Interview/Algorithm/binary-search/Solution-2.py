def search(nums, target):
    # nums: sorted array of int 
    # target: searched item
    # return: index , -1 if not fond
    
    n = len(nums)
    l, r = 0, n-1 
    
    while  l <= r: 
        m = (l+r) // 2
        if nums[m] == target:
            return m
        
        if nums[m] > target:
            r = m 
        else:
            l = m + 1 
            
    return - 1

  # This fixes the issues in Solution-1.py
  # The only difference is on line 9, having **l<= r** v.s. l < r.
