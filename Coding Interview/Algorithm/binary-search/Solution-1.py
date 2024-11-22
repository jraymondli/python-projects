def search(nums, target):
    # nums: sorted array of int 
    # target: searched item
    # return: index , -1 if not fond
    
    n = len(nums)
    l, r = 0, n-1 
    
    while  l < r: 
        m = (l+r) // 2
        if nums[m] == target:
            return m
        
        if nums[m] > target:
            r = m 
        else:
            l = m + 1 
            
    return - 1

  # This code has one issue: it will missed it if we search for the largest number.

  
        
