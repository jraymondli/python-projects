# here is an O(m+n) solution

def find_median_sorted_arrays(nums1, nums2):

  m = len(nums1)
  n = len(nums2)
  
  nums = []
  i = j = 0
  while i < m and j < n:
    if nums1[i] < nums2[j]:
      nums.append(nums1[i])
      i += 1 
    else: 
      nums.append(nums2[j])
      j += 1 
  if i < m:
    nums.extend(nums1[i:])
  if j < n: 
    nums.extend(nums2[j:])
  if (m+n) %2: return nums[(m+n)//2]
  return (nums[(m+n)//2] + nums[(m+n)//2 -1]) / 2 
