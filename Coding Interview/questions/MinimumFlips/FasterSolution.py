def min_flips(s):

    n = len(s)
    
    # Construct the two possible alternating patterns for length 2 * n
    alt1 = ''.join(['0' if i % 2 == 0 else '1' for i in range(2 * n)])
    alt2 = ''.join(['1' if i % 2 == 0 else '0' for i in range(2 * n)])
    
    # Double the string to simulate rotations without actually rotating
    s = s * 2
    
    # Initialize minimum flips required to a large number
    min_flips = float('inf')
    
    # Count the initial differences for the first window of length n
    diff1 = sum(1 for i in range(n) if s[i] != alt1[i])
    diff2 = sum(1 for i in range(n) if s[i] != alt2[i])
    
    # Slide the window across the double-length string
    for i in range(n):
        # Update the minimum flips found
        min_flips = min(min_flips, diff1, diff2)
        
        # Slide the window by removing the effect of the outgoing element and adding the incoming element
        if s[i] != alt1[i]: diff1 -= 1
        if s[i + n] != alt1[i + n]: diff1 += 1
        
        if s[i] != alt2[i]: diff2 -= 1
        if s[i + n] != alt2[i + n]: diff2 += 1
    
    # Ensure to take the minimum after the last window
    min_flips = min(min_flips, diff1, diff2)
    
    return min_flips
