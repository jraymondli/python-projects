def print_unique_permutations(nums):
  
  n = len(nums)
  if n == 0: return []
  if n == 1: return [[nums[0]]]
  
  sub_results = print_unique_permutations(nums[0:-1])
  rt = set()
  for perm in sub_results:
    for i in range(n):
      np = perm[:i] 
      np.append(nums[-1])
      np.extend(perm[i:])
      rt.add(tuple(np))
  
  return [list(tp) for tp in rt]
 
