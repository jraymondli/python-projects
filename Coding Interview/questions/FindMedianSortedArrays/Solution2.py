# O(log(m,n))

def find_median_sorted_arrays(nums1, nums2):

  m = len(nums1)
  n = len(nums2)
  
  if m > n: 
    nums1, nums2 = nums2, nums1 
    m, n = n, m 
  if m == 0:
    if n %2: return nums2[n//2]
    else: return (nums2[n//2] + nums2[n//2 - 1]) / 2 
    
  l, r, half = 0, m, (m+n+1)//2 
  while l <= r: 
    i = (l+r) // 2 
    j = half - i 
    if i > 0 and nums1[i-1] > nums2[j]:
      r = i - 1 
    elif j > 0 and nums2[j-1] > nums1[i]:
      l = i + 1 
    else:
      if i == 0: max_left = nums2[half-1]
      elif j == 0: max_left = nums1[half-1]
      else: max_left = max(nums1[i-1], nums2[j-1])
      if (m+n) %2: return max_left 
      
      if i == m: min_right = nums2[j]
      elif j == n: min_right = nums1[i]
      else: min_right = min(nums1[i], nums2[j])
      return (max_left + min_right) / 2
      
      
      
  
