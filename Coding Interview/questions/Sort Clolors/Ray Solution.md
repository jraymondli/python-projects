def sort_colors(colors):

    nc = len(colors)
    found_none_zero = False
    for i in range(nc):
      if colors[i] != 0: 
        found_none_zero = True
        break  
    if not found_none_zero: return colors 
    
    first_none_zero = i
    for j in range(i+1, nc):
      if colors[j] == 0:
        colors[i], colors[j] = colors[j], colors[i]
        i += 1
        
    complete_loop = True 
    for i in range(nc-1, -1, -1):
      if colors[i] != 2:
        complete_loop = False 
        break 
    for j in range(i-1, -1, -1):
      if colors[j] == 2:
        colors[i], colors[j] = colors[j], colors[i]
        i -= 1 
        
    return colors
