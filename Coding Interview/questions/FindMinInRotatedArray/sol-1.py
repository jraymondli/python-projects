# Using binary search

def find_min_in_rotated_array(arr):

  n = len(arr)
  l, r = 0, n - 1
  while l < r:
    m = (l+r) // 2 
    if arr[m] > arr[r]: l = m + 1
    else: r = m 
  return arr[r]
